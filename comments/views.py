from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters

# from projects.permissions import HasProjectPermission
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsAuthorOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorOrReadOnly,
        # HasProjectPermission,
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('author', 'issue_id')

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(author=user)

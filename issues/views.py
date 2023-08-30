from rest_framework import permissions
from rest_framework import viewsets
from django_filters import rest_framework as filters

from users.models import User

# from projects.permissions import HasProjectPermission
from .models import Issue
from .serializers import IssueSerializer
from .permissions import IsAuthorOrReadOnly


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        # HasProjectPermission,
        IsAuthorOrReadOnly,
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('author', 'is_active')

    def perform_create(self, serializer):
        author = self.request.user
        assignee = self.request.data.get('assignee')
        issue = serializer.save(author=author)
        if assignee:
            try:
                assignee = User.objects.get(username=assignee)
                issue.assignee = assignee
                issue.save()
            except User.DoesNotExist:
                pass

    def get_queryset(self):
        user = self.request.user
        return Issue.objects.filter(author=user)

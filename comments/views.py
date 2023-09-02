from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('author', 'issue_id')

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(author=user)


"""
- Comment
    - Visible que par les contributeurs du projet, mais suppression
            et actualisation uniquement par son auteur.

    - Interdit à tout utilisateur autorisé autre que l'auteur d'émettre
            une requete d'actualisation et suppression d'un issues/project/commentaire.
"""

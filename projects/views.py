from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(contributor=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

"""
- Projects
    - Gestion d'affichage pour contributor --> ok, a voir si il doit les voir, mais ne doit pas pouvoir changer 
            ou s'il ne dois pas les voir. Actuellement tel que c'est configuré,
            il ne voit que si est contributeur du project.

    - Interdit à tout utilisateur autorisé autre que l'auteur d'émettre
            une requete d'actualisation et suppression d'un issues/project/commentaire.
"""

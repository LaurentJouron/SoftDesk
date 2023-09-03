from rest_framework import permissions
from django.db.models import Q
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
        return Project.objects.filter(Q(contributor=user) ^ Q(author=user))

from django.db.models import Q
from rest_framework import permissions
from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsAuthorOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(Q(contributor=user) | Q(author=user)).distinct()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

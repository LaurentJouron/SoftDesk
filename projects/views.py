from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets

# from django_filters import rest_framework as filters

from .models import Project
from .serializers import ProjectSerializer

from .permissions import IsProjectAuthor, IsProjectContributor


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsProjectAuthor | IsProjectContributor,
    ]
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('author', 'is_active')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(author=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

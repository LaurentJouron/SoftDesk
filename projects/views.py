from rest_framework import permissions
from django.db.models import Q
from rest_framework import viewsets

from .models import Project
from .permissions import IsAuthorOrReadOnly
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing projects.

    This ViewSet provides CRUD operations for Project objects, with additional
    filtering to only include active contributors.

    Attributes:
        queryset (QuerySet): The queryset of Project objects.
        serializer_class (ProjectSerializer): The serializer class for Project objects.
        permission_classes (list): The list of permission classes for this view.

    Methods:
        perform_create: Creates a new Project with the requesting user as the author.
        get_queryset: Returns the queryset of Project objects, including active contributors.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        """
        Returns the queryset of Project objects, including projects where the requesting
        user is either the author or an active contributor.

        This method filters the queryset to include projects where the requesting user
        is either the author or an active contributor. It uses the logical OR operator
        to combine these conditions.

        Returns:
            QuerySet: The filtered queryset of Project objects.
        """
        user = self.request.user
        return Project.objects.filter(Q(contributor=user) | Q(author=user)).distinct()

    def perform_create(self, serializer):
        """
        Creates a new Project with the requesting user as the author.

        Args:
            serializer: The serializer containing project data.

        Returns:
            None
        """
        user = self.request.user
        serializer.save(author=user)

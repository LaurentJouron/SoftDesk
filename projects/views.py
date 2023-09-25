from django.db.models import Q
from rest_framework import permissions
from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsAuthorOrReadOnly

class ProjectViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Project instances.

    This viewset provides CRUD operations for Project instances through
    the API. It includes features like filtering projects by contributor
    or author and ensuring that only authenticated users can perform
    certain actions.

    Attributes:
        queryset (QuerySet): The queryset containing all Project instances.
        serializer_class (serializers.Serializer): The serializer class
            used for Project instances.
        permission_classes (list): The list of permission classes required
            for accessing these views.

    Methods:
        get_queryset(): Returns the queryset for the current request.
        perform_create(serializer): Performs the creation of a new project
            instance.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        """
        Returns the queryset for the current request.

        This method customizes the queryset based on the user's role.
        It filters projects to include those where the user is either
        the contributor or the author.

        Returns:
            QuerySet: The filtered queryset.
        """
        user = self.request.user
        qs = self.queryset.filter(Q(contributor=user) | Q(author=user))
        qs = qs.distinct()
        return qs

    def perform_create(self, serializer):
        """
        Performs the creation of a new project instance.

        Args:
            serializer (ProjectSerializer): The serializer instance.
        """
        user = self.request.user
        serializer.save(author=user)
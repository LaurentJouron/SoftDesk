from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects.permissions import HasProjectPermission, IsAuthorOrReadOnly
from projects.models import Project
from .serializers import IssueSerializer


class IssueViewSet(ModelViewSet):
    """
    ViewSet for the Issue model.

    Serializer:
        IssueSerializer: The serializer class for the Issue model.

    Permissions:
        IsAuthenticated: Allows access only to authenticated users.
        HasProjectPermission: Allows access only to users with project-specific permissions.
        IsAuthorOrReadOnly: Allows read-only access to non-authors of the issue.

    Methods:
        get_queryset(self): Retrieves the queryset of issues associated with a project.
    """

    serializer_class = IssueSerializer
    permission_classes = [
        IsAuthenticated,
        HasProjectPermission,
        IsAuthorOrReadOnly,
    ]

    def get_queryset(self):
        """
        Retrieves the queryset of issues associated with a project.

        Returns:
            QuerySet: The queryset of issues.
        """
        project = Project.objects.get(pk=self.kwargs['projects_id'])
        queryset = project.issues.all()
        return queryset

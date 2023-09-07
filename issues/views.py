from rest_framework import permissions
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django.db.models import Q
from users.models import User
from projects.permissions import IsAuthorOrReadOnly
from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing issues.

    This ViewSet provides CRUD operations for Issue objects with specific permissions
    and restrictions.

    Attributes:
        queryset (QuerySet): The queryset of Issue objects.
        serializer_class (IssueSerializer): The serializer class for Issue objects.
        permission_classes (list): The list of permission classes for this view.
        filter_backends (tuple): The tuple of filter backends used for filtering.
        filterset_fields (tuple): The tuple of fields available for filtering.

    Methods:
        perform_create: Creates a new Issue with the requesting user as the author and assigns it to an optional assignee.
        get_queryset: Returns the queryset of Issue objects authored by the requesting user.
    """

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsAuthorOrReadOnly
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ["status"]

    def get_queryset(self):
        """
        Returns the queryset of Issue objects authored by the requesting user.

        Returns:
            QuerySet: The filtered queryset of Issue objects.
        """
        user = self.request.user
        return Issue.objects.filter(Q(author=user) | Q(assignee=user))

    def perform_create(self, serializer):
        """
        Creates a new Issue with the requesting user as the author and assigns it to an optional assignee.

        Args:
            serializer: The serializer containing issue data.

        Returns:
            None
        """
        author = self.request.user
        assignee = self.request.data.get("assignee")
        issue = serializer.save(author=author)
        if assignee:
            try:
                assignee = User.objects.get(username=assignee)
                issue.assignee = assignee
                issue.save()
            except User.DoesNotExist:
                pass

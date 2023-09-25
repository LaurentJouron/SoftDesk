from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters

from issues.models import Issue
from .permissions import IsIssueAuthor
from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Comment instances.

    This viewset provides CRUD operations for Comment instances through
    the API. It includes features like associating comments with issues,
    filtering comments based on the associated project's author and contributors,
    and ensuring that only authorized users (issue authors) can perform certain actions.

    Attributes:
        queryset (QuerySet): The queryset containing all Comment instances.
        serializer_class (serializers.Serializer): The serializer class
            used for Comment instances.
        permission_classes (list): The list of permission classes required
            for accessing these views.

    Methods:
        perform_create(serializer): Performs the creation of a new comment
            instance.
        get_queryset(): Returns the queryset for the current request.

    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsIssueAuthor
    ]
    filter_backends = (filters.DjangoFilterBackend,)

    def perform_create(self, serializer):
        """
        Performs the creation of a new comment instance.

        Args:
            serializer (CommentSerializer): The serializer instance.
        """
        author = self.request.user
        issue = self.kwargs['issue_pk']
        issue = get_object_or_404(Issue, pk=issue)
        serializer.save(author=author, issue=issue)

    def get_queryset(self):
        """
        Returns the queryset for the current request.

        This method customizes the queryset based on the user's role.
        It filters comments to include those related to projects where
        the user is either the author or a contributor.

        Returns:
            QuerySet: The filtered queryset.
        """
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.filter(
            Q(issue__project__author=user) | 
            Q(issue__project__contributor=user)
            )
        return qs

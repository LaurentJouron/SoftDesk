from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from projects.permissions import HasProjectPermission, IsAuthorOrReadOnly
from issues.models import Issue
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments.

    Attributes:
        queryset (QuerySet): The queryset of Comment objects.
        serializer_class (CommentSerializer): The serializer class for Comment objects.
        permission_classes (list): The list of permission classes for the viewset.

    Methods:
        get_queryset(): Get the queryset of comments for a specific issue.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticated,
        HasProjectPermission,
        IsAuthorOrReadOnly,
    ]

    def get_queryset(self):
        """
        Get the queryset of comments for a specific issue.

        Returns:
            QuerySet: The queryset of Comment objects.
        """
        queryset = Issue.objects.get(
            Q(project__id=self.kwargs['project_id'])
            & Q(pk=self.kwargs['issue_id'])
        )
        return queryset.comments.all()

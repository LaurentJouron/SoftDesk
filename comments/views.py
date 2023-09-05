from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments.

    This ViewSet provides CRUD operations for Comment objects with specific permissions
    and filtering options.

    Attributes:
        queryset (QuerySet): The queryset of Comment objects.
        serializer_class (CommentSerializer): The serializer class for Comment objects.
        permission_classes (list): The list of permission classes for this view.
        filter_backends (tuple): The tuple of filter backends used for filtering.
        filterset_fields (tuple): The tuple of fields available for filtering.

    Methods:
        perform_create: Creates a new Comment with the requesting user as the author.
        get_queryset: Returns the queryset of Comment objects authored by the requesting user.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('author', 'issue_id')

    def perform_create(self, serializer):
        """
        Creates a new Comment with the requesting user as the author.

        Args:
            serializer: The serializer containing comment data.

        Returns:
            None
        """
        author = self.request.user
        serializer.save(author=author)

    def get_queryset(self):
        """
        Returns the queryset of Comment objects authored by the requesting user.

        Returns:
            QuerySet: The filtered queryset of Comment objects.
        """
        user = self.request.user
        return Comment.objects.filter(author=user)

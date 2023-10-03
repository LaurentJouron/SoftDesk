from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth import get_user_model

from .models import Comment

User = get_user_model()


class AuthorRelatedField(serializers.SlugRelatedField):
    """
    A SlugRelatedField for selecting the author of an issue.

    This field allows selecting the author of an issue from a list of users.
    The list of users is filtered to include only those who are associated with
    the issue, either as the author of the issue or as an assignee of the
    issue.

    Attributes:
        context (dict): The context passed to the field.

    Methods:
        get_queryset(self): Returns the filtered queryset of possible authors.
    """

    def get_queryset(self):
        """
        Returns the filtered queryset of possible authors.

        This method filters the list of users to include only those who are
        associated with the issue specified in the context. Users are included
        if they are either the author of the issue or an assignee of the issue.

        Returns:
            QuerySet: The filtered queryset of possible authors.
        """
        qs = User.objects.all()
        issue_pk = self.context.get("issue_pk", None)
        if issue_pk:
            qs = qs.filter(
                Q(author__issues__pk=issue_pk) 
                | Q(author__assignee__issue__pk=issue_pk)
            )
        return qs


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.

    This serializer defines how the Comment model is serialized and
    deserialized for use in API views.

    Attributes:
        author (serializers.SlugRelatedField): A field representing the author
            of the comment.
        issue (serializers.SlugRelatedField): A field representing the
        associated issue of the comment.

    Meta:
        model (Comment): The Comment model that this serializer is associated
        with.
        fields (list): The fields to include in the serialized data.

    """

    author = AuthorRelatedField(
        many=False, 
        read_only=True, 
        slug_field="username"
        )
    issue = serializers.SlugRelatedField(read_only=True, slug_field="id")

    class Meta:
        model = Comment
        fields = [
            "id",
            "url",
            "description",
            "author",
            "created",
            "modified",
            "issue",
        ]

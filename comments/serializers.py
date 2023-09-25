from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth import get_user_model

from .models import Comment

User = get_user_model()


class AuthorRelatedField(serializers.SlugRelatedField):
    def get_queryset(self):
        qs = User.objects.all()
        issue_pk = self.context.get("issue_pk", None)
        if issue_pk:
            qs = qs.filter(
                Q(author__issues__pk=issue_pk) | Q(author__assignee__issue__pk=issue_pk)
            )
        return qs


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.

    This serializer defines how the Comment model is serialized and deserialized
    for use in API views.

    Attributes:
        author (serializers.SlugRelatedField): A field representing the author
            of the comment.
        issue (serializers.SlugRelatedField): A field representing the associated
            issue of the comment.

    Meta:
        model (Comment): The Comment model that this serializer is associated with.
        fields (list): The fields to include in the serialized data.

    """

    author = AuthorRelatedField(many=False, read_only=True, slug_field="username")
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

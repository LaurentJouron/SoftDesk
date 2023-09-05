from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.

    This serializer is used to serialize Comment objects to and from JSON.

    Attributes:
        id (IntegerField): The ID of the Comment.
        url (HyperlinkedIdentityField): The URL of the Comment.
        description (TextField): The text content of the Comment.
        author (SlugRelatedField): The username of the author of the Comment.
        created (DateTimeField): The timestamp when the Comment was created.
        modified (DateTimeField): The timestamp when the Comment was last modified.
        issue (SlugRelatedField): The title of the issue to which the Comment is related.

    Methods:
        None
    """

    author = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='username'
    )
    issue = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='title'
    )

    class Meta:
        model = Comment
        fields = [
            'id',
            'url',
            'description',
            'author',
            'created',
            'modified',
            'issue',
        ]

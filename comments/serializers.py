from rest_framework import serializers

from .models import Comment

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

    author = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='username'
    )
    issue = serializers.SlugRelatedField(read_only=True, slug_field='id')

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

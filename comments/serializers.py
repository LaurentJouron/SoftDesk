from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='username'
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

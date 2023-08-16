from rest_framework import serializers
from .models import Comment


class CommentRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'url',
            'description',
            'issue',
            'author',
            'created',
            'modified',
        ]


class CommentIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'url',
            'description',
            'author',
            'created',
            'modified',
        ]

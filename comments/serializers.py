from rest_framework import serializers

from issues.models import Issue
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.

    Attributes:
        owner (ReadOnlyField): The username of the comment's owner.

    Methods:
        create(validated_data): Create and save a new comment instance.

    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = [
            'url',
            'id',
            'description',
            'author_user',
            'issue',
            'created_datetime',
            'modified_datetime',
            'owner',
        ]

    def create(self, validated_data):
        """
        Create and save a new comment instance.

        Args:
            validated_data (dict): Validated data for creating the comment.

        Returns:
            Comment: The newly created comment instance.

        """
        author = self.context.get('request', None).user

        issue = Issue.objects.get(
            pk=self.context.get('view').kwargs['issue_id']
        )

        comment = Comment.objects.create(
            description=validated_data['description'],
            author=author,
            issue=issue,
        )

        comment.save()
        return comment

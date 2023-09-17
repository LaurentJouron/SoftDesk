from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Issue, TagChoice, PriorityChoice, StatusChoice

User = get_user_model()


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Issue model.

    This serializer is used to serialize Issue objects to and from JSON.

    Attributes:
        id (IntegerField): The ID of the Issue.
        url (HyperlinkedIdentityField): The URL of the Issue.
        title (CharField): The title of the Issue.
        description (TextField): The description of the Issue.
        tag (SlugRelatedField): The tag associated with the Issue.
        priority (SlugRelatedField): The priority associated with the Issue.
        status (SlugRelatedField): The status of the Issue.
        created (DateTimeField): The timestamp when the Issue was created.
        modified (DateTimeField): The timestamp when the Issue was last modified.
        is_active (BooleanField): Indicates whether the Issue is active or not.
        author (ReadOnlyField): The username of the author of the Issue.
        assignee (SlugRelatedField): The username of the user assigned to the Issue.
        project (PrimaryKeyRelatedField): The ID of the project to which the Issue belongs.
        comments (HyperlinkedRelatedField): A list of hyperlinked related comments.

    Methods:
        __str__: Returns a textual representation of the Issue.
    """

    author = serializers.ReadOnlyField(source="author.username")
    assignee = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field="username",
        queryset=User.objects.all(),
    )
    comments = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="comment-detail"
    )
    tag = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=TagChoice.objects.all()
    )
    priority = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=PriorityChoice.objects.all()
    )
    status = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=StatusChoice.objects.all()
    )
    project = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = Issue
        fields = [
            "id",
            "url",
            "title",
            "description",
            "tag",
            "priority",
            "status",
            "created",
            "modified",
            "is_active",
            "author",
            "assignee",
            "project",
            "comments",
        ]

    def __str__(self):
        """
        Returns a textual representation of the Issue.

        Returns:
            str: The title of the Issue.
        """
        return self.title

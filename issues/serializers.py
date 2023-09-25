from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth import get_user_model

from .models import Issue, TagChoice, PriorityChoice, StatusChoice

User = get_user_model()


class AssigneeRelatedField(serializers.SlugRelatedField):
    """
    Custom SlugRelatedField for assigning users to issues.

    This field is used to represent and validate the assignee of an issue.
    It filters the list of possible assignees based on the project's contributors
    and authors.

    Methods:
        get_queryset(): Returns the filtered queryset of possible assignees.

    """

    def get_queryset(self):
        """
        Returns the filtered queryset of possible assignees.

        Returns:
            QuerySet: The filtered queryset of possible assignees.
        """
        qs = User.objects.all()
        project_pk = self.context.get("project_pk", None)
        if project_pk:
            qs = qs.filter(
                Q(contributed_projects__pk=project_pk) | Q(projects__pk=project_pk),
                is_active=True,
            )
        return qs


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Issue model.

    This serializer defines how the Issue model is serialized and deserialized
    for use in API views.

    Attributes:
        author (serializers.ReadOnlyField): A field representing the username
            of the author.
        assignee (AssigneeRelatedField): A field representing the assignee of
            the issue.
        comments (serializers.HyperlinkedRelatedField): A field representing
            related comments.
        tag (serializers.SlugRelatedField): A field representing the tag of the
            issue.
        priority (serializers.SlugRelatedField): A field representing the priority
            of the issue.
        status (serializers.SlugRelatedField): A field representing the status
            of the issue.
        project (serializers.PrimaryKeyRelatedField): A field representing the
            project to which the issue belongs.

    Meta:
        model (Issue): The Issue model that this serializer is associated with.
        fields (list): The fields to include in the serialized data.

    """

    author = serializers.ReadOnlyField(source="author.username")
    assignee = AssigneeRelatedField(
        many=False,
        read_only=False,
        slug_field="username",
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
    project = serializers.PrimaryKeyRelatedField(read_only=True)

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
        String representation of the issue.

        Returns:
            str: The title of the issue.
        """
        return self.title

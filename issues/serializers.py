from rest_framework import serializers

from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    """
    Serializer for the Issue model.

    Fields:
        url (HyperlinkedIdentityField): The endpoint URL for the issue.
        id (IntegerField): The unique identifier for the issue.
        title (CharField): The title of the issue.
        description (TextField): The description of the issue.
        tag_choices (CharField): The tag choice for the issue (Bug, Feature, Task).
        priority_choices (CharField): The priority choice for the issue (Low, Medium, High).
        status_choices (CharField): The status choice for the issue (To do, In progress, Finished).
        author (PrimaryKeyRelatedField): The user who created the issue.
        assigned_user (PrimaryKeyRelatedField): The user assigned to the issue.
        created_time (DateTimeField): The timestamp when the issue was created.
        modified_datetime (DateTimeField): The timestamp when the issue was last modified.

    Read-Only Fields:
        author (PrimaryKeyRelatedField): The user who created the issue.
        project (PrimaryKeyRelatedField): The project associated with the issue.
        created_time (DateTimeField): The timestamp when the issue was created.

    Methods:
        create(self, validated_data): Creates and returns a new Issue instance.
        update(self, instance, validated_data): Updates and returns an existing Issue instance.
    """

    class Meta:
        model = Issue
        fields = [
            'url',
            'id',
            'title',
            'description',
            'tag_choices',
            'priority_choices',
            'status_choices',
            'author',
            'assigned_user',
            'created_time',
            'modified_datetime',
        ]
        read_only_fields = [
            'author',
            'project',
            'created_time',
        ]

    def create(self, validated_data):
        """
        Creates and returns a new Issue instance.

        Args:
            validated_data (dict): The validated data for the new Issue.

        Returns:
            Issue: The created Issue instance.
        """
        return Issue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates and returns an existing Issue instance.

        Args:
            instance (Issue): The existing Issue instance to update.
            validated_data (dict): The validated data for updating the Issue.

        Returns:
            Issue: The updated Issue instance.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.tag_choices = validated_data.get(
            'tag_choices', instance.tag_choices
        )
        instance.priority_choices = validated_data.get(
            'priority_choices', instance.priority_choices
        )
        instance.status_choices = validated_data.get(
            'status_choices', instance.status_choices
        )
        instance.created_time = validated_data.get(
            'created_time', instance.created_time
        )
        instance.modified_datetime = validated_data.get(
            'modified_datetime', instance.modified_datetime
        )
        instance.project = validated_data.get('project', instance.project)
        instance.author = validated_data.get('author', instance.author)
        instance.created_time = validated_data.get(
            'created_time', instance.created_time
        )
        instance.save()
        return instance

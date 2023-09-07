from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Project, TypeChoice

User = get_user_model()


class TypeChoiceSerializer(serializers.ModelSerializer):
    """
    Serializer for the TypeChoice model.

    This serializer is used to serialize TypeChoice objects to and from JSON.

    Attributes:
        id (IntegerField): The ID of the TypeChoice.
        name (CharField): The name of the TypeChoice.
    """

    class Meta:
        model = TypeChoice
        fields = ("id", "name")


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Project model.

    This serializer is used to serialize Project objects to and from JSON.

    Attributes:
        url (HyperlinkedIdentityField): The URL of the Project.
        id (IntegerField): The ID of the Project.
        author (ReadOnlyField): The username of the author of the Project.
        title (CharField): The title of the Project.
        description (CharField): The description of the Project.
        type_choice (SlugRelatedField): The type choice associated with the Project.
        contributor (SlugRelatedField): The usernames of contributors to the Project.
        created (DateTimeField): The timestamp when the Project was created.
        modified (DateTimeField): The timestamp when the Project was last modified.
        issues (HyperlinkedRelatedField): A list of hyperlinked related issues.

    Methods:
        __str__: Returns a textual representation of the Project.
    """

    author = serializers.ReadOnlyField(source="author.username")
    contributor = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field="username",
    )
    type_choice = serializers.SlugRelatedField(
        queryset=TypeChoice.objects.all(), many=False, slug_field="name"
    )

    class Meta:
        model = Project
        fields = [
            "url",
            "id",
            "author",
            "title",
            "description",
            "type_choice",
            "contributor",
            "created",
            "modified",
            "issues",
        ]

    def __str__(self):
        """
        Returns a textual representation of the Project.

        Returns:
            str: The title of the Project.
        """
        return self.title

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Project, TypeChoice

User = get_user_model()


class TypeChoiceSerializer(serializers.ModelSerializer):
    """
    Serializer for the TypeChoice model.

    This serializer defines how the TypeChoice model is serialized
    and deserialized for use in API views.

    Meta:
        model (TypeChoice): The TypeChoice model that this serializer
            is associated with.
        fields (tuple): The fields to include in the serialized data.

    """

    class Meta:
        model = TypeChoice
        fields = ("id", "name")


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Project model.

    This serializer defines how the Project model is serialized and
    deserialized for use in API views.

    Attributes:
        author (serializers.ReadOnlyField): A field representing the
            username of the author.
        contributor (serializers.SlugRelatedField): A field representing
            the contributors' usernames.
        type_choice (serializers.SlugRelatedField): A field representing
            the project's type.
        issues (serializers.HyperlinkedRelatedField): A field representing
            related issues.

    Meta:
        model (Project): The Project model that this serializer is
            associated with.
        fields (list): The fields to include in the serialized data.

    """

    author = serializers.ReadOnlyField(source="author.username")
    contributor = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.filter(is_active=True, is_staff=True),
        slug_field="username",
    )
    type_choice = serializers.SlugRelatedField(
        queryset=TypeChoice.objects.all(), many=False, slug_field="name"
    )
    issues = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="issue-detail"
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "url",
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
        String representation of the project.

        Returns:
            str: The title of the project.
        """
        return self.title

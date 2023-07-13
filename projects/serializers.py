from rest_framework import serializers
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.

    Fields:
        url (HyperlinkedIdentityField): The endpoint URL for the project.
        id (IntegerField): The unique identifier for the project.
        highlight (HyperlinkedIdentityField): The URL for the highlighted project in HTML format.
        is_active (BooleanField): Indicates whether the project is active or not.
        created_datetime (DateTimeField): The timestamp when the project was created.
        modified_datetime (DateTimeField): The timestamp when the project was last modified.
        title (CharField): The title of the project.
        description (TextField): The description of the project.
        type_choice (CharField): The type choice for the project (Back-end, Front-end, iOS, Android).
        is_active (BooleanField): Indicates whether the project is active or not.
        author (PrimaryKeyRelatedField): The user who created the project.
        owner (ReadOnlyField): The username of the owner of the project.

    Methods:
        create(self, validated_data): Creates and returns a new Project instance.
        update(self, instance, validated_data): Updates and returns an existing Project instance.
        save(self, *args, **kwargs): Saves the Project instance and performs additional actions.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    """
    ReadOnlyField: The username of the owner of the project.
    """

    highlight = serializers.HyperlinkedIdentityField(
        view_name='project-highlight', format='html'
    )
    """
    HyperlinkedIdentityField: The URL for the highlighted project in HTML format.
    """

    class Meta:
        model = Project
        fields = [
            'url',
            'id',
            'highlight',
            'is_active',
            'created_datetime',
            'modified_datetime',
            'title',
            'description',
            'type_choice',
            'is_active',
            'author',
            'owner',
        ]
        """
        Meta options for the ProjectSerializer.

        Attributes:
            model (Project): The model class associated with the serializer.
            fields (list[str]): The fields to include in the serialized representation.
        """

    def create(self, validated_data):
        """
        Creates and returns a new Project instance.

        Args:
            validated_data (dict): The validated data for the new Project.

        Returns:
            Project: The created Project instance.
        """
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates and returns an existing Project instance.

        Args:
            instance (Project): The existing Project instance to update.
            validated_data (dict): The validated data for updating the Project.

        Returns:
            Project: The updated Project instance.
        """
        instance.created_datetime = validated_data.get(
            'created_datetime', instance.created_datetime
        )
        instance.modified_datetime = validated_data.get(
            'modified_datetime', instance.modified_datetime
        )
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.type_choice = validated_data.get(
            'type_choice', instance.type_choice
        )
        instance.is_active = validated_data.get(
            'is_active', instance.is_active
        )
        instance.author = validated_data.get('author', instance.author)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    def save(self, *args, **kwargs):
        """
        Saves the Project instance and performs additional actions.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        instance = super().save(*args, **kwargs)
        type_choice = instance.type_choice
        is_active = 'table' if instance.is_active else False
        options = {'title': instance.title} if instance.title else {}
        formatter = HtmlFormatter(
            style=self.style, is_active=is_active, full=True, **options
        )
        lexer = get_lexer_by_name(type_choice)
        self.highlighted = highlight(instance.created, lexer, formatter)
        super().save(*args, **kwargs)

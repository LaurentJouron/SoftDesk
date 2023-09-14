from rest_framework import serializers
from django.db.models import Q

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the User model.

    This serializer is used to serialize User objects to and from JSON.

    Attributes:
        projects (HyperlinkedRelatedField): A list of hyperlinked related projects.
        password1 (CharField): The first password input field (write-only).
        password2 (CharField): The second password input field (write-only).

    Methods:
        validate: Validates the input data and ensures that the passwords match.
        create: Creates a new User object with the provided data.
        update: Updates an existing User object with the provided data.
    """

    projects = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='project-detail',
        source='projects_contributed',
    )
    password1 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )

    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'projects',
            'password1',
            'password2',
        ]

    def validate(self, data):
        """
        Validates the input data.

        This method checks if the passwords match.

        Args:
            data (dict): The input data.

        Returns:
            dict: The validated data.

        Raises:
            serializers.ValidationError: If the passwords don't match.
        """
        if (
            data["password1"]
            and data["password2"]
            and data["password1"] != data["password2"]
        ):
            raise serializers.ValidationError("Password mismatch")
        return data

    def create(self, validated_data):
        """
        Creates a new User object.

        This method creates a new User object with the provided data.

        Args:
            validated_data (dict): The validated data.

        Returns:
            User: The created User object.
        """
        password1 = validated_data.pop("password1")
        password2 = validated_data.pop("password2")
        user = User.objects.create_user(password=password1, **validated_data)
        return user

    def update(self, instance, validated_data):
        """
        Updates an existing User object.

        This method updates an existing User object with the provided data.

        Args:
            instance (User): The existing User object.
            validated_data (dict): The validated data.

        Returns:
            User: The updated User object.
        """
        password1 = validated_data.pop("password1")
        password2 = validated_data.pop("password2")
        instance.set_password(password1)
        super().update(instance, validated_data)
        instance.save()
        return instance

class UserProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'email',
        ]

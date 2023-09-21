from rest_framework import serializers

from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the User model.

    This serializer defines how the User model is serialized and deserialized
    for use in API views.

    Attributes:
        projects (serializers.HyperlinkedRelatedField): A field representing
            the user's contributed projects.
        password1 (serializers.CharField): A field for the first password input.
        password2 (serializers.CharField): A field for the second password input.

    Meta:
        model (User): The User model that this serializer is associated with.
        fields (list): The list of fields to include in the serialized data.

    Methods:
        validate(data): Validates the input data, checking if passwords match.
        create(validated_data): Creates a new user instance.
        update(instance, validated_data): Updates an existing user instance.

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
        Creates a new user instance.

        Args:
            validated_data (dict): The validated data for creating a new user.

        Returns:
            User: The newly created user instance.
        """
        password1 = validated_data.pop("password1")
        password2 = validated_data.pop("password2")
        user = User.objects.create_user(password=password1, **validated_data)
        return user

    def update(self, instance, validated_data):
        """
        Updates an existing user instance.

        Args:
            instance (User): The existing user instance to update.
            validated_data (dict): The validated data for updating the user.

        Returns:
            User: The updated user instance.
        """
        password1 = validated_data.pop("password1")
        password2 = validated_data.pop("password2")
        instance.set_password(password1)
        super().update(instance, validated_data)
        instance.save()
        return instance

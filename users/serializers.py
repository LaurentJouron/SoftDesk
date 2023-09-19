from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
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
        password1 = validated_data.pop("password1")
        password2 = validated_data.pop("password2")
        user = User.objects.create_user(password=password1, **validated_data)
        return user

    def update(self, instance, validated_data):
        password1 = validated_data.pop("password1")
        password2 = validated_data.pop("password2")
        instance.set_password(password1)
        super().update(instance, validated_data)
        instance.save()
        return instance

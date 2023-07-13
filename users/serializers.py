from django.contrib.auth.models import User
from rest_framework import serializers
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Fields:
        url (HyperlinkedIdentityField): The endpoint URL for the user.
        id (IntegerField): The unique identifier for the user.
        username (CharField): The username of the user.
        first_name (CharField): The first name of the user.
        last_name (CharField): The last name of the user.
        email (EmailField): The email address of the user.
        password (CharField): The password of the user.
        projects (HyperlinkedRelatedField): The related projects of the user.
        is_active (BooleanField): Indicates whether the user is active or not.
        is_superuser (BooleanField): Indicates whether the user is a superuser or not.
        is_staff (BooleanField): Indicates whether the user is a staff member or not.
        date_joined (DateTimeField): The timestamp when the user joined.

    Methods:
        create(self, validated_data): Creates and returns a new User instance.
        update(self, instance, validated_data): Updates and returns an existing User instance.
        save(self, *args, **kwargs): Saves the User instance and performs additional actions.
    """

    projects = serializers.HyperlinkedRelatedField(
        many=True, view_name='project-detail', read_only=True
    )
    """
    HyperlinkedRelatedField: The related projects of the user.
    """

    password = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )
    """
    CharField: The password of the user (write-only).
    """

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'projects',
            'is_active',
            'is_superuser',
            'is_staff',
            'date_joined',
        ]
        """
        Meta options for the UserSerializer.

        Attributes:
            model (User): The model class associated with the serializer.
            fields (list[str]): The fields to include in the serialized representation.
        """

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Creates and returns a new User instance.

        Args:
            validated_data (dict): The validated data for the new User.

        Returns:
            User: The created User instance.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates and returns an existing User instance.

        Args:
            instance (User): The existing User instance to update.
            validated_data (dict): The validated data for updating the User.

        Returns:
            User: The updated User instance.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.projects = validated_data.get('projects', instance.projects)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.save()
        return instance

    def save(self, *args, **kwargs):
        """
        Saves the User instance and performs additional actions.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        instance = super().save(*args, **kwargs)
        is_active = 'table' if instance.is_active else False
        options = {'username': instance.username} if instance.username else {}
        formatter = HtmlFormatter(style=self.style, is_active=is_active, full=True, **options)
        lexer = get_lexer_by_name('first_name')
        self.highlighted = highlight(instance.created, lexer, formatter)
        super().save(*args, **kwargs)

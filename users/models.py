from django.db import models


class User(models.Model):
    """
    Represents a user in the system.

    Fields:
    - username: The username of the user (max length: 150 characters, unique)
    - email: The email address of the user (unique)
    - is_active: Whether the user account is active (default: True)
    - is_staff: Whether the user is a staff member (default: True)
    - is_superuser: Whether the user has superuser privileges (default: False)

    Methods:
    - __str__: Returns the username as the string representation of the user.
    """

    username = models.CharField(
        max_length=150, unique=True, help_text="The username of the user"
    )
    email = models.EmailField(
        unique=True, help_text="The email address of the user"
    )
    is_active = models.BooleanField(
        default=True, help_text="Whether the user account is active"
    )
    is_staff = models.BooleanField(
        default=True, help_text="Whether the user is a staff member"
    )
    is_superuser = models.BooleanField(
        default=False, help_text="Whether the user has superuser privileges"
    )

    def __str__(self):
        """
        Returns the username as the string representation of the user.
        """
        return self.username

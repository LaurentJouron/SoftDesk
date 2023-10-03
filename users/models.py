from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.

    This model represents a user in the application. It extends the
    default Django User model to include additional fields.

    Attributes:
        username (str): The unique username for the user.
        email (str): The unique email address associated with the user.

    Methods:
        __str__(): Returns a string representation of the user.

    """

    email = models.EmailField(unique=True)

    def __str__(self):
        """
        String representation of the user.

        Returns:
            str: The username of the user.
        """
        return self.username

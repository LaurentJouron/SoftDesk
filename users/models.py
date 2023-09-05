from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom model for users.

    This model extends the `AbstractUser` class from Django to add a unique email field.

    Attributes:
        email (EmailField): The unique email address of the user.
    """

    email = models.EmailField(unique=True)

    def __str__(self):
        """
        Returns a textual representation of the user.

        Returns:
            str: Username of the user.
        """
        return self.username

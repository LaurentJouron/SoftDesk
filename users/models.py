from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from projects.models import Project


class User(AbstractUser):
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

    project_contributors = models.ManyToManyField(
        Project,
        through='users.ProjectContributor',
        related_name='contributed_users',
    )

    def __str__(self):
        return self.username


class ProjectContributor(models.Model):
    PERMISSION_CHOICES = [
        ('AUTHOR', 'Author'),
        ('CONTRIBUTORS', 'Contributor'),
    ]
    permission = models.CharField(
        choices=PERMISSION_CHOICES,
        max_length=20,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f'{self.user.username} - {self.project.title}'

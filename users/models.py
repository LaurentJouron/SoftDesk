from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Represents a user in the system.

    Fields:
    - email: The email address of the user (unique)
    Methods:
    - __str__: Returns the username as the string representation of the user.
    """

    email = models.EmailField(
        unique=True, help_text="The email address of the user"
    )

    project_contributors = models.ManyToManyField(
        'projects.Project',
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
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f'{self.user.username} - {self.project.title}'

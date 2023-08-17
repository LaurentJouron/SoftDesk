from django.db import models
from django.utils.translation import gettext_lazy as _


class Contributor(models.Model):
    PERMISSION_CHOICES = [
        ('AUTHOR', 'Author'),
        ('CONTRIBUTORS', 'Contributor'),
    ]
    permission = models.CharField(
        choices=PERMISSION_CHOICES,
        max_length=20,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="related_users",
        related_name='contributors',
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="related_projects",
    )
    role = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} - {self.project.title}'

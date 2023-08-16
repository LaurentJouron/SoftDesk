from django.db import models
from django.contrib.auth.models import User

PERMISSION_CHOICES = [
    ('AUTHOR', 'Author'),
    ('CONTRIBUTORS', 'Contributor'),
]


class Contributor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="contributor"
    )
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    permission = models.CharField(choices=PERMISSION_CHOICES, max_length=20)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} - {self.project.title}'

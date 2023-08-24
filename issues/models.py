from django.db import models
from django.conf import settings


class Issue(models.Model):
    TAG_CHOICES = [
        ('Bug', 'Bug'),
        ('Feature', 'Feature'),
        ('Task', 'Task'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('To do', 'To do'),
        ('In progress', 'In progress'),
        ('Finished', 'Finished'),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    tag_choices = models.CharField(choices=TAG_CHOICES, max_length=20)
    priority_choices = models.CharField(
        choices=PRIORITY_CHOICES, max_length=20
    )
    status_choices = models.CharField(choices=STATUS_CHOICES, max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issues_created',
    )
    project = models.ForeignKey(
        'projects.Project', related_name='issues', on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='issues_assigned',
    )

    def __str__(self):
        return f'{self.title}'

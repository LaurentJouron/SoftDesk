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
    assignee = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='assigned_issues',
    )
    project = models.ForeignKey(
        'projects.Project', related_name='issues', on_delete=models.CASCADE
    )
    issue_comments = models.ManyToManyField(
        'comments.Comment', related_name='related_issue_comments', blank=True
    )

    def __str__(self):
        return f'{self.title}'

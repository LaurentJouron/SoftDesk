from django.db import models
from django.conf import settings


class PriorityChoice(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TagChoice(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class StatusChoice(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    priority = models.ForeignKey(
        'issues.PriorityChoice',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="issues_priority",
    )
    tag = models.ForeignKey(
        'issues.TagChoice',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="issues_tags",
    )
    status = models.ForeignKey(
        'issues.StatusChoice',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="issues_status",
    )
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

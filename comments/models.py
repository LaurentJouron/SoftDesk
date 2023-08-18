from django.db import models
from django.conf import settings


class Comment(models.Model):
    description = models.TextField(max_length=2048)
    related_issue = models.ForeignKey(
        'issues.Issue',
        related_name='related_comments',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='authored_comments',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment #{self.pk} on Issue #{self.issue.pk}'

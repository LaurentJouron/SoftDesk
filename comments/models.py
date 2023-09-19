from django.db import models
from django.conf import settings

class Comment(models.Model):
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='author',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    issue = models.ForeignKey(
        'issues.Issue', related_name='comments', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.description

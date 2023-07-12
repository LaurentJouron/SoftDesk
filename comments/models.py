from django.db import models
from django.conf import settings


class Comment(models.Model):
    description = models.CharField(max_length=2048)
    author_user = models.OneToOneField(
        'users.User', on_delete=models.SET(settings.AUTH_USER_MODEL)
    )
    issue = models.OneToOneField(
        'issues.Issue', on_delete=models.SET(settings.AUTH_USER_MODEL)
    )
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_datetime']

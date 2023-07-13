from django.db import models
from django.conf import settings

from issues.models import Issue


class Comment(models.Model):
    """
    Model representing a comment on an issue.

    Attributes:
        description (str): The description of the comment.
        author_user (User): The user who wrote the comment.
        issue (Issue): The issue to which the comment is associated.
        created_datetime (datetime): The date and time when the comment was created.
        modified_datetime (datetime): The date and time of the last modification of the comment.
    """

    description = models.TextField(max_length=2048)
    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.RESTRICT
    )
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, related_name='comments'
    )
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_datetime']

from django.db import models
from django.conf import settings

class Comment(models.Model):
    """
    Model for representing comments on issues.

    This model represents comments made by users on issues in your application.
    It includes the comment's description, author, creation and modification
    timestamps, and the issue to which the comment belongs.

    Attributes:
        description (str): The text content of the comment.
        author (User): The user who authored the comment.
        created (datetime): The timestamp when the comment was created.
        modified (datetime): The timestamp when the comment was last modified.
        issue (Issue): The issue to which the comment is associated.

    Methods:
        __str__(): Returns a string representation of the comment.

    """

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
        """
        String representation of the comment.

        Returns:
            str: The text content of the comment.
        """
        return self.description

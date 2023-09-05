from django.db import models
from django.conf import settings

class Comment(models.Model):
    """
    Model to represent a comment.

    This model represents a comment with various attributes such as description,
    author, timestamps, and the associated issue.

    Attributes:
        description (TextField): The text content of the comment.
        author (ForeignKey): The author of the comment.
        created (DateTimeField): The timestamp when the comment was created.
        modified (DateTimeField): The timestamp when the comment was last modified.
        issue (ForeignKey): The issue to which the comment is related.

    Methods:
        __str__: Returns a textual representation of the comment.
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
        Returns a textual representation of the comment.

        Returns:
            str: The text content of the comment.
        """
        return self.description

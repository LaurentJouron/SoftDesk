from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

from projects.models import Project


class Contributor(models.Model):
    """
    Model representing a contributor in a project.

    Attributes:
        user (ForeignKey): The user associated with the contributor.
        project (ForeignKey): The project the contributor is associated with.
    """

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='contributor_id',
    )
    """
    ForeignKey: The user associated with the contributor.
    """

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='contributors',
    )
    """
    ForeignKey: The project the contributor is associated with.
    """

from django.db import models
from django.conf import settings
from projects.models import Project

class PriorityChoice(models.Model):
    """
    Model for defining issue priority choices.

    This model represents the available priority choices for issues.

    Attributes:
        name (str): The name of the priority choice.

    Methods:
        __str__(): Returns a string representation of the priority choice.

    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        String representation of the priority choice.

        Returns:
            str: The name of the priority choice.
        """
        return self.name


class TagChoice(models.Model):
    """
    Model for defining issue tag choices.

    This model represents the available tag choices for issues.

    Attributes:
        name (str): The name of the tag choice.

    Methods:
        __str__(): Returns a string representation of the tag choice.

    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        String representation of the tag choice.

        Returns:
            str: The name of the tag choice.
        """
        return self.name


class StatusChoice(models.Model):
    """
    Model for defining issue status choices.

    This model represents the available status choices for issues.

    Attributes:
        name (str): The name of the status choice.

    Methods:
        __str__(): Returns a string representation of the status choice.

    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        String representation of the status choice.

        Returns:
            str: The name of the status choice.
        """
        return self.name


class Issue(models.Model):
    """
    Model for representing issues.

    This model represents issues, including their title, description, priority,
    tag, status, creation and modification timestamps, author, project, and assignee.

    Attributes:
        title (str): The title of the issue.
        description (str): The description of the issue.
        priority (PriorityChoice): The priority of the issue (optional).
        tag (TagChoice): The tag associated with the issue (optional).
        status (StatusChoice): The status of the issue (optional).
        created (datetime): The timestamp when the issue was created.
        modified (datetime): The timestamp when the issue was last modified.
        is_active (bool): Whether the issue is active or not.
        author (User): The user who created the issue.
        project (Project): The project to which the issue belongs.
        assignee (User): The user assigned to the issue (optional).

    Methods:
        __str__(): Returns a string representation of the issue.

    """

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
        Project, related_name='issues', on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='issues_assigned',
    )

    def __str__(self):
        """
        String representation of the issue.

        Returns:
            str: The title of the issue.
        """
        return f'{self.title}'

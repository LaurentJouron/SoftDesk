from django.db import models
from django.conf import settings


class PriorityChoice(models.Model):
    """
    Model to represent priority choices for issues.

    This model is used to represent different priority choices that can be associated
    with issues.

    Attributes:
        name (CharField): The name of the priority choice.

    Methods:
        __str__: Returns a textual representation of the priority choice.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        Returns a textual representation of the priority choice.

        Returns:
            str: The name of the priority choice.
        """
        return self.name


class TagChoice(models.Model):
    """
    Model to represent tag choices for issues.

    This model is used to represent different tag choices that can be associated
    with issues.

    Attributes:
        name (CharField): The name of the tag choice.

    Methods:
        __str__: Returns a textual representation of the tag choice.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        Returns a textual representation of the tag choice.

        Returns:
            str: The name of the tag choice.
        """
        return self.name


class StatusChoice(models.Model):
    """
    Model to represent status choices for issues.

    This model is used to represent different status choices that can be associated
    with issues.

    Attributes:
        name (CharField): The name of the status choice.

    Methods:
        __str__: Returns a textual representation of the status choice.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        Returns a textual representation of the status choice.

        Returns:
            str: The name of the status choice.
        """
        return self.name


class Issue(models.Model):
    """
    Model to represent an issue.

    This model represents an issue with various attributes such as title, description,
    priority, tag, status, author, project, and assignee.

    Attributes:
        title (CharField): The title of the issue.
        description (TextField): The description of the issue.
        priority (ForeignKey): The priority associated with the issue.
        tag (ForeignKey): The tag associated with the issue.
        status (ForeignKey): The status of the issue.
        created (DateTimeField): The timestamp when the issue was created.
        modified (DateTimeField): The timestamp when the issue was last modified.
        is_active (BooleanField): Indicates whether the issue is active or not.
        author (ForeignKey): The author of the issue.
        project (ForeignKey): The project to which the issue belongs.
        assignee (ForeignKey): The user assigned to the issue.

    Methods:
        __str__: Returns a textual representation of the issue.
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
        'projects.Project', related_name='issues', on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='issues_assigned',
    )

    def __str__(self):
        """
        Returns a textual representation of the issue.

        Returns:
            str: The title of the issue.
        """
        return f'{self.title}'

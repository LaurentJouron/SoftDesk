from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

TAG_CHOICES = [
    ('Bug', 'Bug'),
    ('Feature', 'Feature'),
    ('Task', 'Task'),
]
PRIORITY_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]
STATUS_CHOICES = [
    ('To do', 'To do'),
    ('In progress', 'In progress'),
    ('Finished', 'Finished'),
]


class Issue(models.Model):
    """
    Model representing an issue in a project.

    Attributes:
        title (CharField): The title of the issue.
        description (TextField): The description of the issue.
        tag_choices (CharField): The tag choice for the issue (Bug, Feature, Task).
        priority_choices (CharField): The priority choice for the issue (Low, Medium, High).
        status_choices (CharField): The status choice for the issue (To do, In progress, Finished).
        created_time (DateTimeField): The timestamp when the issue was created.
        modified_datetime (DateTimeField): The timestamp when the issue was last modified.
        author (ForeignKey): The user who created the issue.
        assigned_user (ForeignKey): The user assigned to the issue.
    """

    title = models.CharField(max_length=128)
    """
    CharField: The title of the issue.
    """

    description = models.TextField(max_length=2048)
    """
    TextField: The description of the issue.
    """

    tag_choices = models.CharField(choices=TAG_CHOICES, max_length=10)
    """
    CharField: The tag choice for the issue (Bug, Feature, Task).
    """

    priority_choices = models.CharField(
        choices=PRIORITY_CHOICES, max_length=10
    )
    """
    CharField: The priority choice for the issue (Low, Medium, High).
    """

    status_choices = models.CharField(choices=STATUS_CHOICES, max_length=12)
    """
    CharField: The status choice for the issue (To do, In progress, Finished).
    """

    created_time = models.DateTimeField(auto_now_add=True)
    """
    DateTimeField: The timestamp when the issue was created.
    """

    modified_datetime = models.DateTimeField(auto_now=True)
    """
    DateTimeField: The timestamp when the issue was last modified.
    """

    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_created',
    )
    """
    ForeignKey: The user who created the issue.
    """

    assigned_user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_assigned',
    )
    """
    ForeignKey: The user assigned to the issue.
    """

    def __str__(self):
        """
        Returns a string representation of the issue.

        Returns:
            str: The title of the issue.
        """
        return f'{self.title}'

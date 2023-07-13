from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

TYPE_CHOICES = [
    ('BACK-END', 'Back-end'),
    ('FRONT-END', 'Front-end'),
    ('IOS', 'iOS'),
    ('ANDROID', 'Android'),
]


class Project(models.Model):
    """
    Model representing a project.

    Attributes:
        created_datetime (DateTimeField): The timestamp when the project was created.
        modified_datetime (DateTimeField): The timestamp when the project was last modified.
        title (CharField): The title of the project.
        description (TextField): The description of the project.
        type_choice (CharField): The type choice for the project (Back-end, Front-end, iOS, Android).
        is_active (BooleanField): Indicates whether the project is active or not.
        author (ForeignKey): The user who created the project.
    """

    created_datetime = models.DateTimeField(auto_now_add=True)
    """
    DateTimeField: The timestamp when the project was created.
    """

    modified_datetime = models.DateTimeField(auto_now=True)
    """
    DateTimeField: The timestamp when the project was last modified.
    """

    title = models.CharField(max_length=100)
    """
    CharField: The title of the project.
    """

    description = models.TextField(max_length=2000)
    """
    TextField: The description of the project.
    """

    type_choice = models.CharField(choices=TYPE_CHOICES, max_length=20)
    """
    CharField: The type choice for the project (Back-end, Front-end, iOS, Android).
    """

    is_active = models.BooleanField(default=True)
    """
    BooleanField: Indicates whether the project is active or not.
    """

    author = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='projects'
    )
    """
    ForeignKey: The user who created the project.
    """

    def __str__(self):
        """
        Returns a string representation of the project.

        Returns:
            str: The title of the project.
        """
        return f'{self.title}'

    class Meta:
        """
        Meta options for the Project model.

        Attributes:
            ordering (list[str]): The ordering of projects by created datetime.
        """

        ordering = ['created_datetime']

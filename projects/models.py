from django.db import models
from django.conf import settings


class TypeChoice(models.Model):
    """
    Model to represent types of choices.

    This model is used to represent different types of choices that can be associated
    with projects.

    Attributes:
        name (CharField): The name of the choice.

    Methods:
        __str__: Returns a textual representation of the choice.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        Returns a textual representation of the choice.

        Returns:
            str: The name of the choice.
        """
        return self.name


class Project(models.Model):
    """
    Model to represent a project.

    This model represents a project with various attributes such as title, description,
    type_choice, author, contributors, and timestamps.

    Attributes:
        title (CharField): The title of the project.
        description (CharField): The description of the project.
        type_choice (ForeignKey): The type of choice associated with the project.
        created (DateTimeField): The timestamp when the project was created.
        modified (DateTimeField): The timestamp when the project was last modified.
        author (ForeignKey): The author of the project.
        contributor (ManyToManyField): The contributors to the project.

    Methods:
        __str__: Returns a textual representation of the project.
    """

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    type_choice = models.ForeignKey(
        "projects.TypeChoice",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="projects",
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="projects",
        on_delete=models.CASCADE,
    )
    contributor = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="contributed_projects",
    )

    def __str__(self):
        """
        Returns a textual representation of the project.

        Returns:
            str: The title of the project.
        """
        return self.title

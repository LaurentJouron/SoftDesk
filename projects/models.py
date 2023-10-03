from django.db import models
from django.conf import settings


class TypeChoice(models.Model):
    """
    Model for defining project types.

    This model represents the various types that a project can belong to.

    Attributes:
        name (str): The name of the project type.

    Methods:
        __str__(): Returns a string representation of the project type.

    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        String representation of the project type.

        Returns:
            str: The name of the project type.
        """
        return self.name


class Project(models.Model):
    """
    Model for representing projects.

    This model represents projects, including their title, description,
    type, creation and modification timestamps, author, and contributors.

    Attributes:
        title (str): The title of the project.
        description (str): The description of the project.
        type_choice (TypeChoice): The type of the project (optional).
        created (datetime): The timestamp when the project was created.
        modified (datetime): The timestamp when the project was last modified.
        author (User): The user who created the project.
        contributor (User): The users who have contributed to the project
        (optional).

    Methods:
        __str__(): Returns a string representation of the project.

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
        String representation of the project.

        Returns:
            str: The title of the project.
        """
        return self.title

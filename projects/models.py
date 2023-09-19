from django.db import models
from django.conf import settings


class TypeChoice(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
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
        return self.title

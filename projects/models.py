from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Project(models.Model):
    TYPE_CHOICES = [
        ('BACK-END', 'Back-end'),
        ('FRONT-END', 'Front-end'),
        ('IOS', 'iOS'),
        ('ANDROID', 'Android'),
    ]
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    type_choices = models.CharField(choices=TYPE_CHOICES, max_length=40)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="related user (author)",
        related_name='projects',
        on_delete=models.CASCADE,
        help_text=_(
            "Each project has an author. This author is a user who can have multiple projects"
        ),
    )

    def __str__(self):
        return self.title

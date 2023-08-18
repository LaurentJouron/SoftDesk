# Generated by Django 4.2.4 on 2023-08-18 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("projects", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("description", models.TextField(max_length=2048)),
                (
                    "tag_choices",
                    models.CharField(
                        choices=[
                            ("Bug", "Bug"),
                            ("Feature", "Feature"),
                            ("Task", "Task"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "priority_choices",
                    models.CharField(
                        choices=[
                            ("Low", "Low"),
                            ("Medium", "Medium"),
                            ("High", "High"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "status_choices",
                    models.CharField(
                        choices=[
                            ("To do", "To do"),
                            ("In progress", "In progress"),
                            ("Finished", "Finished"),
                        ],
                        max_length=20,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "assignee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_issues",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issues_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issues",
                        to="projects.project",
                    ),
                ),
            ],
        ),
    ]

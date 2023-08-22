# Generated by Django 4.2.4 on 2023-08-22 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("issues", "0001_initial"),
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="issue",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issues_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="issue",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issues",
                to="projects.project",
            ),
        ),
    ]

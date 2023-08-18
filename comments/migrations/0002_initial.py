# Generated by Django 4.2.4 on 2023-08-18 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("comments", "0001_initial"),
        ("issues", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="issue",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="issues.issue",
            ),
        ),
    ]

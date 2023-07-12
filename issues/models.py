from django.db import models

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
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    tag_choices = models.CharField(choices=TAG_CHOICES, max_length=10)
    priority_choices = models.CharField(
        choices=PRIORITY_CHOICES, max_length=10
    )
    status_choices = models.CharField(choices=STATUS_CHOICES, max_length=12)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

from django.db import models
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

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
    tag_choices = models.CharField(choices=TAG_CHOICES, max_length=20)
    priority_choices = models.CharField(
        choices=PRIORITY_CHOICES, max_length=20
    )
    status_choices = models.CharField(choices=STATUS_CHOICES, max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='issues_created'
    )
    assignee = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_issues',
    )
    project = models.ForeignKey(
        'projects.Project', related_name='issues', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        is_active = 'table' if self.is_active else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(
            style='vs', is_active=is_active, full=True, **options
        )
        lexer = get_lexer_by_name('python')
        self.highlighted = highlight(self.description, lexer, formatter)
        super(Issue, self).save(*args, **kwargs)

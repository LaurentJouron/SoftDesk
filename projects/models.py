from re import escape
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

TYPE_CHOICES = [
    ('BACK-END', 'Back-end'),
    ('FRONT-END', 'Front-end'),
    ('IOS', 'iOS'),
    ('ANDROID', 'Android'),
]


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    type_choices = models.CharField(choices=TYPE_CHOICES, max_length=40)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        'auth.User', related_name='projects', on_delete=models.CASCADE
    )
    contributors = models.ManyToManyField(
        'auth.User', related_name='projects_contributed'
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        active_style = 'table' if self.is_active else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(
            style='vs', is_active=active_style, full=True, **options
        )
        escaped_description = escape(self.description)
        lexer = get_lexer_by_name('python')
        self.highlighted = highlight(escaped_description, lexer, formatter)
        super(Project, self).save(*args, **kwargs)

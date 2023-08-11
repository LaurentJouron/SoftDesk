from re import escape
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name


from django.db import models


class Comment(models.Model):
    description = models.TextField(max_length=2048)
    issue = models.ForeignKey(
        'issues.Issue', related_name='comments', on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        'auth.User', related_name='authored_comments', on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    highlighted = models.TextField()

    def __str__(self):
        return f'Comment #{self.pk} on Issue #{self.issue.pk}'

    def save(self, *args, **kwargs):
        options = {'description': self.description} if self.description else {}
        formatter = HtmlFormatter(
            style='vs', is_active=False, full=True, **options
        )
        escaped_description = escape(self.description)
        lexer = get_lexer_by_name('python')
        self.highlighted = highlight(escaped_description, lexer, formatter)
        super(Comment, self).save(*args, **kwargs)

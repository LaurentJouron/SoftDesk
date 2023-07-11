from django.db import models

TYPE_CHOICES = [
    ('BACK-END', 'Back-end'),
    ('FRONT-END', 'Front-end'),
    ('IOS', 'iOS'),
    ('ANDROID', 'Android'),
]


class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    type_choice = models.CharField(choices=TYPE_CHOICES, max_length=20)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['created']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

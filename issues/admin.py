from django.contrib import admin

from .models import Issue, TagChoice, PriorityChoice, StatusChoice

admin.site.register(Issue)
admin.site.register(TagChoice)
admin.site.register(PriorityChoice)
admin.site.register(StatusChoice)

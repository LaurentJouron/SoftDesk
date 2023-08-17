from django.urls import path
from . import views

urlpatterns = [
    path(
        'issues/<int:issue_pk>/comments/',
        views.IssueViewSet.as_view(),
        name='issue-comments',
    ),
]

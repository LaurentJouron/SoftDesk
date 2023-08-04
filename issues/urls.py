from django.urls import path
from . import views

urlpatterns = [
    path(
        'issues/<int:issue_pk>/comments/',
        views.IssueCommentsView.as_view(),
        name='issue-comments',
    ),
]

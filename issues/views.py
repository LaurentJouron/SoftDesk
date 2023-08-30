from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from users.models import User
from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        author = self.request.user
        assignee = self.request.data.get('assignee')
        issue = serializer.save(author=author)
        if assignee:
            try:
                assignee = User.objects.get(username=assignee)
                issue.assignee = assignee
                issue.save()
            except User.DoesNotExist:
                pass

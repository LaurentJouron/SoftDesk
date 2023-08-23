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
        assignee_data = self.request.data.get('assignee')
        if isinstance(author, get_user_model()):
            issue = serializer.save(author=author)
            if assignee_data:
                try:
                    assignee = User.objects.get(id=assignee_data)
                    issue.assignee = assignee
                    issue.save()
                except User.DoesNotExist:
                    pass
        else:
            serializer.save()

    def get_queryset(self):
        return self.queryset.filter(
            project_id=self.kwargs.get('project_id')
        ).filter(author=self.request.user)

from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import User
from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        issue = self.get_object()
        return Response(issue.highlighted)

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

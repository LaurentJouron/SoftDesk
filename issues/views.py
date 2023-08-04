from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users import permissions
from comments.serializers import CommentSerializer
from comments.models import Comment
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
        if isinstance(author, get_user_model()):
            serializer.save(author=author)
        else:
            serializer.save()


class IssueCommentsView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        issue_pk = self.kwargs.get('issue_pk')
        return Comment.objects.filter(issue_id=issue_pk)

    def perform_create(self, serializer):
        issue_pk = self.kwargs.get('issue_pk')
        serializer.save(issue_id=issue_pk)

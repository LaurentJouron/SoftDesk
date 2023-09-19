from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters

from issues.models import Issue
from .permissions import IsIssueAuthor
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsIssueAuthor
    ]
    filter_backends = (filters.DjangoFilterBackend,)

    def perform_create(self, serializer):
        author = self.request.user
        issue = self.kwargs['issue_pk']
        issue = get_object_or_404(Issue, pk=issue)
        serializer.save(author=author, issue=issue)

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(Q(issue__project__author=user) | Q(issue__project__contributor=user))

from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets
from django_filters import rest_framework as filters

from users.models import User
from projects.models import Project
from .permissions import IsProjectAuthorOrContributor
from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsProjectAuthorOrContributor
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ["status"]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(Q(project__author=user) | Q(project__contributor=user)).distinct()

    def perform_create(self, serializer):
        author = self.request.user
        project = self.kwargs['project_pk']
        project = get_object_or_404(Project, pk=project)
        issue = serializer.save(author=author, project=project)
        assignee = self.request.data.get("assignee")
        if assignee:
            try:
                assignee = User.objects.get(username=assignee)
                issue.assignee = assignee
                issue.save()
            except User.DoesNotExist:
                pass

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["project_pk"] = self.kwargs['project_pk']
        return context
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters import rest_framework as filters

from users.models import User
from projects.models import Project
from .permissions import IsProjectAuthorOrContributor
from .models import Issue
from .serializers import IssueSerializer

class IssueViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Issue instances.

    This viewset provides CRUD operations for Issue instances through
    the API. It includes features like filtering issues by status and
    ensuring that only authorized users (project authors and contributors)
    can perform certain actions.

    Attributes:
        queryset (QuerySet): The queryset containing all Issue instances.
        serializer_class (serializers.Serializer): The serializer class
            used for Issue instances.
        permission_classes (list): The list of permission classes required
            for accessing these views.

    Methods:
        get_queryset(): Returns the queryset for the current request.
        perform_create(serializer): Performs the creation of a new issue
            instance.
        get_serializer_context(): Returns the context for the serializer.
    """

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsProjectAuthorOrContributor
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ["status"]

    def get_queryset(self):
        """
        Returns the queryset for the current request.

        This method customizes the queryset based on the user's role.
        It filters issues to include those related to projects where
        the user is either the author or a contributor.

        Returns:
            QuerySet: The filtered queryset.
        """
        user = self.request.user
        queryset = Issue.objects.filter(Q(project__author=user) | Q(project__contributor=user)).distinct()
        return queryset

    def perform_create(self, serializer):
        """
        Performs the creation of a new issue instance.

        Args:
            serializer (IssueSerializer): The serializer instance.
        """
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
                return Response(issue, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                pass

    def get_serializer_context(self):
        """
        Returns the context for the serializer.

        Returns:
            dict: The context for the serializer.
        """
        context = super().get_serializer_context()
        context["project_pk"] = self.kwargs['project_pk']
        return context

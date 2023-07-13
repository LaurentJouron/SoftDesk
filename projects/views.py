from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import renderers

from contributors.models import Contributor
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsProjectOwner, IsProjectContributor


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Project model.

    Attributes:
        queryset (QuerySet): The queryset of projects.
        serializer_class (ProjectSerializer): The serializer class for the Project model.
        permission_classes (list): The list of permission classes for the viewset.

    Methods:
        highlight(self, request, *args, **kwargs): Retrieves the highlighted project in HTML format.
        perform_create(self, serializer): Performs additional actions when creating a project.
        get_queryset(self): Retrieves the queryset of projects based on user permissions.
    """

    queryset = Project.objects.all()
    """
    QuerySet: The queryset of projects.
    """

    serializer_class = ProjectSerializer
    """
    ProjectSerializer: The serializer class for the Project model.
    """

    permission_classes = [
        IsAuthenticated,
        IsProjectOwner | IsProjectContributor,
    ]
    """
    list: The list of permission classes for the viewset.
    """

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        """
        Retrieves the highlighted project in HTML format.

        Args:
            request (HttpRequest): The incoming request.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The response containing the highlighted project in HTML format.
        """
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        """
        Performs additional actions when creating a project.

        Args:
            serializer (ProjectSerializer): The serializer instance.

        Returns:
            None
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Retrieves the queryset of projects based on user permissions.

        Returns:
            QuerySet: The queryset of projects.
        """
        contributor = Contributor.object.filter(user=self.request.user)
        queryset = Project.objects.filter(
            Q(author=self.request.user) | Q(contributors__in=contributor)
        )
        return queryset.distinct()

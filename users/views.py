from rest_framework import permissions
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer
from .models import ProjectContributor
from .serializers import ContributorSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed (Read-only).

    This viewset provides endpoints to list and retrieve users.

    List Users:
    - Retrieve a paginated list of all users in the system.

    Retrieve User:
    - Retrieve detailed information about a specific user identified by its ID.

    Response Status Codes:
    - 200 OK: Request successful.
    - 401 Unauthorized: Authentication credentials were not provided.
    - 403 Forbidden: You do not have permission to access this resource.

    Security:
    - List Users: Requires authentication.
    - Retrieve User: Requires authentication.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAuthenticated,
    ]


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = ProjectContributor.objects.all()
    serializer_class = ContributorSerializer

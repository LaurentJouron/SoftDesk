from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework import viewsets

from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed (Read-only).
    This viewset provides endpoints to list and retrieve users.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAuthenticated,
    ]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all users.",
        responses={200: UserSerializer(many=True)},
        security=[],
    )
    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of all users.
        This endpoint returns a paginated list of all users in the system.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve a specific user by ID.",
        responses={200: UserSerializer()},
        security=[],
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific user by ID.
        This endpoint returns detailed information about a specific user identified by its ID.
        """
        return super().retrieve(request, *args, **kwargs)

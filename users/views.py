from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
)

from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for the User model.

    Attributes:
        queryset (QuerySet): The queryset of users.
        serializer_class (UserSerializer): The serializer class for the User model.
    """

    queryset = User.objects.all()
    """
    QuerySet: The queryset of users.
    """

    serializer_class = UserSerializer
    """
    UserSerializer: The serializer class for the User model.
    """


class UserView(APIView):
    """
    API view to retrieve user information.

    Attributes:
        authentication_classes (list): The list of authentication classes for the view.
        permission_classes (list): The list of permission classes for the view.
    """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    """
    list: The list of authentication classes for the view.
    """

    permission_classes = [IsAuthenticated]
    """
    list: The list of permission classes for the view.
    """

    def get(self, request, format=None):
        """
        Retrieves user information.

        Args:
            request (HttpRequest): The incoming request.
            format (str, optional): The format of the response. Defaults to None.

        Returns:
            Response: The response containing the user information.
        """
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)

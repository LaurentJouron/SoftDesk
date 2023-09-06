from rest_framework import permissions
from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import User
from .permissions import IsOwnUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the User model.

    This ViewSet provides CRUD operations for User objects.

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (UserSerializer): The serializer class for User objects.
        permission_classes (list): The list of permission classes for this view.
        filter_backends (tuple): The tuple of filter backends used for filtering.

    Methods:
        get_queryset: Returns the queryset of User objects, filtered for non-superusers.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated | IsOwnUser
    ]
    
    def get_queryset(self):
        """
        Returns the queryset of User objects, filtered for non-superusers.

        This method filters the queryset to only include User objects that are not superusers.

        Returns:
            QuerySet: The filtered queryset of User objects.
        """
        user = self.request.user

        if user.is_superuser:
            return self.queryset
        # return self.queryset.filter(pk=user.pk)
        return self.queryset.all()

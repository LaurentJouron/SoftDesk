from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnProfile


class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing User instances.

    This viewset provides CRUD operations for User instances through
    the API. It includes features like filtering by username and
    activation status.

    Attributes:
        queryset (QuerySet): The queryset containing all User instances.
        serializer_class (serializers.Serializer): The serializer class
            used for User instances.
        permission_classes (list): The list of permission classes required
            for accessing these views.
        filter_backends (tuple): The backend used for filtering.
        filterset_fields (tuple): The fields available for filtering.

    Methods:
        get_queryset(): Returns the queryset for the current request.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated, IsOwnProfile
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('username', 'is_active')
    
    def get_queryset(self):
        """
        Returns the queryset for the current request.

        This method customizes the queryset based on the user's role.
        Superusers can view all User instances, while regular users
        can only view their own profile.

        Returns:
            QuerySet: The filtered queryset.
        """
        user = self.request.user
        qs = super().get_queryset()

        if not user.is_superuser:
            return qs.filter(pk=user.pk)
        return qs

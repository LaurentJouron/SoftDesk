from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import User
from .serializers import UserSerializer, UserProjectSerializer
from .permissions import IsOwnProfile

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

    queryset = User.objects.filter(is_active=True, is_staff=True)
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated, IsOwnProfile
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('username', 'is_active')
    
    def get_queryset(self):
        """
        Returns the queryset of User objects, filtered for non-superusers and your custom filter.

        This method filters the queryset to only include User objects that are not superusers
        and meet your custom filter conditions.

        Returns:
            QuerySet: The filtered queryset of User objects.
        """
        user = self.request.user
        qs = super().get_queryset()

        if not user.is_superuser:
            return qs.filter(pk=user.pk)
        return qs
    
class UserProjectViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True, is_staff=True)
    serializer_class = UserProjectSerializer
    permission_classes = [
        IsAuthenticated, IsOwnProfile
    ]

    def get_users(self):
        queryset = User.objects.filter(Q(projects__id=project_id) | Q(contributed_projects__id=project_id))
        project_id = self.request.GET.get('project_id')
        serializer = UserSerializer(queryset, many=True)
        return serializer.data
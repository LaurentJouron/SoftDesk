from rest_framework import permissions
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user)

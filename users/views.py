from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import generics


from .serializers import UserSerializer, UserRegistrationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

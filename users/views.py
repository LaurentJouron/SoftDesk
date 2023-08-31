from rest_framework import permissions
from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(username=user)

        """
        - Authentification des utilisateurs
            - models.py           --> ok
            - serializers.py      --> ok
            - Inscription         --> ok, mais à voir si l'inscription doit se faire hors connexion
            - Connexion           --> ok
            - Utilisation de JWT  --> ok

        Point de terminaison:
            - méthode: POST
                - Inscription de l'utilisateur: /signup/    # A date: http://127.0.0.1:8000/api-auth/login/?next=/
                - Connexion de l'utilisateur: /login/       # A date: http://127.0.0.1:8000/users/
        """

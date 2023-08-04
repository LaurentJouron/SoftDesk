from django.urls import path

from users.views import UserViewSet, UserRegistrationAPIView


urlpatterns = [
    path(
        '',
        UserViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='user-list',
    ),
    path(
        'users/<int:pk>/',
        UserViewSet.as_view(
            {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
        ),
        name='user-detail',
    ),
    path(
        'register/',
        UserRegistrationAPIView.as_view(),
        name='user-registration',
    ),
]

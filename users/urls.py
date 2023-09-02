from django.urls import path

from users.views import UserViewSet


urlpatterns = [
    path(
        '',
        UserViewSet.as_view({'get': 'list'}),
        name='user-list',
    ),
    path(
        '<int:pk>/',
        UserViewSet.as_view(
            {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
        ),
        name='user-detail',
    ),
]

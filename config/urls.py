from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.views import UserViewSet
from contributors.views import ContributorViewSet
from projects.views import ProjectViewSet
from issues.views import IssueViewSet
from comments.views import CommentViewSet


# Gestion des accès aux applications
router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'projects', ProjectViewSet, basename="project")
router.register(r'contributors', ContributorViewSet, basename="contributor")
router.register(r'issues', IssueViewSet, basename="issue")
router.register(r'comments', CommentViewSet, basename="comment")

urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('users.urls')),
]

# Documentation avec Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version='v1',
        description="This API is used to manage todos",
        contact=openapi.Contact(email="djangopython@hotmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path(
        'swagger<format>/',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]

# Authentification et gestion des Tokens
urlpatterns += [
    path(
        'api-auth/', include('rest_framework.urls', namespace='rest_framework')
    ),
    path(
        'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from users.views import UserViewSet
from projects.views import ProjectViewSet
from issues.views import IssueViewSet
from comments.views import CommentViewSet


# Applications router
router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'projects', ProjectViewSet, basename="project")
router.register(r'issues', IssueViewSet, basename="issue")
router.register(r'comments', CommentViewSet, basename="comment")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/', include('users.urls')),
]

# Authentification and Token management
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

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

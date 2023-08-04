from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from users.views import UserViewSet
from contributors.views import ContributorViewSet
from projects.views import ProjectViewSet
from issues.views import IssueViewSet
from comments.views import CommentViewSet

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

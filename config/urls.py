from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)
from rest_framework_nested import routers

from projects.views import ProjectViewSet
from issues.views import IssueViewSet, IssueReadOnlyViewSet
from comments.views import CommentViewSet, CommentReadOnlyViewSet
from users.views import UserViewSet

# Nested URLs
router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register("issues", IssueReadOnlyViewSet)
router.register("comments", CommentReadOnlyViewSet)
router.register("users", UserViewSet)

# Issues under projets
projects_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
projects_router.register(r"issues", IssueViewSet, basename="project-issues")

# Users under projets
projects_router.register(r"users", UserViewSet, basename="project-users")

# Comments under issues
issues_router = routers.NestedSimpleRouter(projects_router, "issues", lookup="issue")
issues_router.register(r"comments", CommentViewSet, basename="issue-comments")

# Base and admin Router
urlpatterns = [
    path("admin/", admin.site.urls),
]

# Router applications
urlpatterns += [
    path(r"", include(router.urls)),
    path(r"", include(projects_router.urls)),
    path(r"", include(issues_router.urls)),
]

# Authentification and Token management
urlpatterns += [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "api/token/blacklist/",
        TokenBlacklistView.as_view(),
        name="token_blacklist",
    ),
]

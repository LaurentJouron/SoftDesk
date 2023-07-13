from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from projects.views import ProjectViewSet
from issues.views import IssueViewSet
from comments.views import CommentViewSet

# Create a router instance
router = routers.DefaultRouter(trailing_slash=True)

# Register viewsets with the router
router.register('projects', ProjectViewSet, basename='projects')
router.register(
    r'projects/(?P<project_id>[^/.]+)/issues', IssueViewSet, basename='issues'
)
router.register(
    r'projects/(?P<project_id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments',
    CommentViewSet,
    basename='comments',
)

# Define the URL patterns
urlpatterns = [
    path('api/', include(router.urls)),
]

# Additional URL patterns
urlpatterns += [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(
        'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
]

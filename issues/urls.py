# from django.urls import path, include
# from rest_framework_nested import routers
# from comments.views import CommentViewSet
# from .views import Issue

# router = routers.SimpleRouter()
# router.register(r'projects', ProjectViewSet)

# projects_router = routers.NestedSimpleRouter(
#     router, r'projects', lookup='project'
# )
# projects_router.register(
#     r'comments', CommentViewSet, basename='project-issues'
# )

# urlpatterns = [
#     path('', include(router.urls)),
#     path('', include(projects_router.urls)),
# ]

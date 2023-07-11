from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects import views

router = DefaultRouter()
router.register(r'project', views.ProjectViewSet, basename="project")

urlpatterns = [
    path('', include(router.urls)),
]

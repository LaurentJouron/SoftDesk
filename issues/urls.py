from django.urls import path, include
from rest_framework.routers import DefaultRouter
from issues import views

router = DefaultRouter()
router.register(r'issues', views.IssueViewSet, basename="issue")

urlpatterns = [
    path('', include(router.urls)),
]

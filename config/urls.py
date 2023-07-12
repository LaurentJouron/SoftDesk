from django.urls import path, include

urlpatterns = [
    path('', include('projects.urls')),
    path('', include('issues.urls')),
    path('', include('comments.urls')),
    path('', include('users.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

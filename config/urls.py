from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)
from rest_framework_nested import routers

from projects.views import ProjectViewSet
from issues.views import IssueViewSet
from comments.views import CommentViewSet
from users.views import UserViewSet

# URLs imbriquées
router = routers.SimpleRouter()
router.register('projects', ProjectViewSet)
router.register('issues', IssueViewSet)
router.register('comments', CommentViewSet)
router.register('user', UserViewSet)

# Issues sous les projets
router.register("issues", IssueViewSet)
projects_router = routers.NestedSimpleRouter(
    router, 'projects', lookup='project'
)
projects_router.register('issues', IssueViewSet, basename='project-issues')

# Commentaires sous les issues
issues_router = routers.NestedSimpleRouter(
    projects_router, 'issues', lookup='issue'
)
issues_router.register('comments', CommentViewSet, basename='issue-comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]

# Applications router
urlpatterns += [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(issues_router.urls)),
]

# Authentification and Token management
urlpatterns += [
    path(
        'api-auth/', include('rest_framework.urls', namespace='rest_framework')
    ),
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
    path(
        'api/token/blacklist/',
        TokenBlacklistView.as_view(),
        name='token_blacklist',
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

"""
Point de terminaison:
    - méthode: GET
        - Récupérer la liste de projet rattaché à l'utilisateur connecté: /projects/ 
        - Récupérer les détails d'un projet via son id: /projects/{id}/
        - Récupérer la liste de tous les utilisateur attaché à un projet: /projects/{id}/users/
        - Récupérer la liste des issues lié à un projet: /projects/{id}/issues/
        - Récupérer la liste des commentaires liés à un issues: /projects/{id}/issues/{id}/comments/
        - Récupérer un commentaire via son id: /projects/{id}/issues/{id}/comments/{id}

    - méthode: POST
        - Création d'un utilisateur: /signup/
        - Connexion de l'utilisateur: /login/
        - Création d'un projet: /projects/
        - Création d'un contributeur à un projet: /projects/{id}/users/
        - Création d'un issue dans un projet: /projects/{id}/issues/
        - Création d'un commentaire sur un issue: /projects/{id}/issues/comments/

    - méthode: PUT
        - Mettre à jour un projet: /projects/{id}/
        - Mettre à jour un issue: /projects/{id}/issues/{id}
        - Mettre à jour un comment: /projects/{id}/issues/{id}/comments/{id}
        
    - méthode: DELETE
        - Supprimer un projet et ses issues: /projects/{id}/
        - Supprimer un utilisateur d'un projet: /projects/{id}/users/{id}
        - Supprimer un issue d'un projet: /projects/{id}/issues/{id}
        - Supprimer un comment: /projects/{id}/issues/{id}/comments/{id}
"""

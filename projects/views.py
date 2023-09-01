from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(contributor=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

        """
        - Projects
            - models.py                            --> ok
            - serializers.py                       --> ok
            - CRUD                                 --> ok
            - Association des issues               --> ok

            - Gestion d'affichage pour contributor --> ok, a voir si il doit les voir, mais ne doit pas pouvoir changer 
                    ou s'il ne dois pas les voir. Actuellement tel que c'est configuré,
                    il ne voit que si est contributeur du project.

            - Interdit à tout utilisateur autorisé autre que l'auteur d'émettre
                    une requete d'actualisation et suppression d'un issues/project/commentaire.

        Point de terminaison:
            - méthode: GET
                - Récupérer la liste de projet rattaché à l'utilisateur connecté: /projects/                    # A date: http://127.0.0.1:8000/projects/   --> ok
                - Récupérer les détails d'un projet via son id: /projects/{id}/                                 # A date: http://127.0.0.1:8000/projects/1/ --> ok
                - Récupérer la liste de tous les utilisateur attaché à un projet: /projects/{id}/users/         # A date: ???
                - Récupérer la liste des issues lié à un projet: /projects/{id}/issues/                         # A date: http://127.0.0.1:8000/issues/     --> NO
                - Récupérer la liste des commentaires liés à un issues: /projects/{id}/issues/{id}/comments/    # A date: http://127.0.0.1:8000/comments/   --> NO
                - Récupérer un commentaire via son id: /projects/{id}/issues/{id}/comments/{id}                 # A date: http://127.0.0.1:8000/comments/1/ --> NO

            - méthode: POST
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

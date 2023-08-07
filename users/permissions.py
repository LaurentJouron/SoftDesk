from rest_framework import permissions
from projects.models import Project


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsProjectAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ['create', 'list']:
            return True
        if view.action in ['retrieve', 'update', 'destroy']:
            project_id = view.kwargs.get('project_pk')
            if project_id:
                project = Project.objects.filter(pk=project_id).first()
                return request.user == project.author
        return False


class IsProjectContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ['create', 'list']:
            return True
        if view.action in ['retrieve', 'update', 'destroy']:
            project_id = view.kwargs.get('project_pk')
            if project_id:
                project = Project.objects.filter(pk=project_id).first()
                return project.contributors.filter(user=request.user).exists()
        return False


class HasProjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view):
        if view.action in ['create', 'list']:
            return True
        if view.action in ['retrieve', 'update', 'destroy']:
            project = view.get_object()
            return (
                request.user == project.author
                or request.user in project.contributors.all()
            )
        return False


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view):
        if view.action in ['create', 'list', 'retrieve']:
            return True
        if view.action in ['update', 'destroy']:
            comment = view.get_object()
            return request.user == comment.author
        return False


class IsAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

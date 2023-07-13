from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from comments.models import Comment
from projects.models import Project


class IsProjectOwner(BasePermission):
    """
    Permission class to allow only project owners certain actions.

    Methods:
        has_permission(self, request, view): Checks if the user has permission to perform the action.
    """

    def has_permission(self, request, view):
        """
        Checks if the user has permission to perform the action.

        Args:
            request (HttpRequest): The incoming request.
            view (View): The view being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        allowed_actions = ['create', 'list']
        if view.action in allowed_actions:
            return True
        allowed_actions = ['retrieve', 'update', 'destroy']
        if view.action in allowed_actions:
            project = get_object_or_404(Project, pk=view.kwargs['pk'])
            return request.user.is_author(project)
        else:
            return False


class IsProjectContributor(BasePermission):
    """
    Permission class to allow only project contributors certain actions.

    Methods:
        has_permission(self, request, view): Checks if the user has permission to perform the action.
    """

    def has_permission(self, request, view):
        """
        Checks if the user has permission to perform the action.

        Args:
            request (HttpRequest): The incoming request.
            view (View): The view being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        allowed_actions = ['list']
        if view.action in allowed_actions:
            return True
        allowed_actions = ['retrieve']
        if view.action in allowed_actions:
            project = get_object_or_404(Project, pk=view.kwargs['pk'])
            return request.user.is_contributor(project)
        else:
            return False


class HasProjectPermission(BasePermission):
    """
    Permission class to allow only users with project-specific permissions certain actions.

    Methods:
        has_permission(self, request, view): Checks if the user has permission to perform the action.
    """

    def has_permission(self, request, view):
        """
        Checks if the user has permission to perform the action.

        Args:
            request (HttpRequest): The incoming request.
            view (View): The view being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        allowed_actions = ['create', 'list', 'retrieve', 'update', 'destroy']
        if view.action in allowed_actions:
            project = get_object_or_404(Project, pk=view.kwargs['project_id'])
            if request.user.is_author(project):
                return True
            if request.user.is_contributor(project):
                return True
        else:
            return False


class IsAuthorOrReadOnly(BasePermission):
    """
    Permission class to allow only the author of a comment certain actions.

    Methods:
        has_permission(self, request, view): Checks if the user has permission to perform the action.
    """

    def has_permission(self, request, view):
        """
        Checks if the user has permission to perform the action.

        Args:
            request (HttpRequest): The incoming request.
            view (View): The view being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        allowed_actions = ['create', 'list', 'retrieve']
        if view.action in allowed_actions:
            return True

        allowed_actions = ['update', 'destroy']
        if view.action in allowed_actions:
            comment = get_object_or_404(Comment, pk=view.kwargs['pk'])
            return request.user.is_author(comment)

        else:
            return False

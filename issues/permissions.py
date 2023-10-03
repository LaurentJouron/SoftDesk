from rest_framework import permissions


class IsProjectAuthorOrContributor(permissions.BasePermission):
    """
    Custom permission to check if the user is the project author or a
    contributor.

    This permission class is used to determine whether a user has permission
    to access and modify a specific issue. Users can access and modify issues
    if they are either the author of the project or a contributor to the
    project.

    Methods:
        has_object_permission(request, view, obj): Check if the user has
            permission for the specified issue object.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission for the specified issue object.

        Args:
            request (Request): The request object.
            view (View): The view being accessed.
            obj: The object being accessed (in this case, an issue).

        Returns:
            bool: True if the user is the author of the project or a
            contributor, False otherwise.
        """
        if obj.project.author == request.user:
            return True
        elif obj.project.contributor.filter(pk=request.user.pk).exists():
            return True

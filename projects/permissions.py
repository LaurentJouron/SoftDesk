from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to check if the user is the author or has read-only access.

    This permission class is used to determine whether a user has permission
    to modify a project instance. Users can only modify projects if they are
    the author; otherwise, they have read-only access.

    Methods:
        has_object_permission(request, view, obj): Check if the user has
            permission for the specified object.

    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission for the specified object.

        Args:
            request (Request): The request object.
            view (View): The view being accessed.
            obj: The object being accessed (in this case, a project).

        Returns:
            bool: True if the user is the author or the request is safe
            (read-only), False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

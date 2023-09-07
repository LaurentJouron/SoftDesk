from rest_framework import permissions

class IsOwnProfile(permissions.BasePermission):
    """
    Custom permission to only allow access to own user profile.

    This permission class restricts access to a user's own profile, ensuring
    that a user can only view and edit their own profile information. It checks
    if the object (profile) being accessed matches the currently authenticated user.

    Attributes:
        None

    Methods:
        has_object_permission: Check if the user has permission to access the object.
    """
    def has_object_permission(self, request, view, obj):
        """
        Determine if the user has permission to access the object.

        This method checks if the currently authenticated user is the owner of the
        object (profile) being accessed. Users are only allowed to view and edit
        their own profile.

        Args:
            request: The HTTP request being made.
            view: The view requesting access to the object.
            obj: The object (user profile) being accessed.

        Returns:
            bool: True if the user has permission to access the object, False otherwise.
        """
        return obj == request.user

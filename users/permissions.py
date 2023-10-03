from rest_framework import permissions


class IsOwnProfile(permissions.BasePermission):
    """
    Custom permission to check if the user owns the profile.

    This permission class is used to determine whether a user has
    permission to access or modify a profile. It checks if the user
    making the request is the owner of the profile.

    Methods:
        has_object_permission(request, view, obj): Check if the user
            has permission for the specified object.

    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission for the specified object.

        Args:
            request (Request): The request object.
            view (View): The view being accessed.
            obj: The object being accessed (in this case, a user profile).

        Returns:
            bool: True if the user is the owner of the profile, False
            otherwise.
        """
        return obj.author == request.user

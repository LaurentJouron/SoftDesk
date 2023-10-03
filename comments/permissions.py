from rest_framework import permissions


class IsIssueAuthor(permissions.BasePermission):
    """
    Custom permission to check if the user is the author of the associated
    issue.

    This permission class is used to determine whether a user has permission
    to access and modify a specific comment. Users can access and modify
    comments
    only if they are the author of the issue to which the comment belongs or if
    they are a contributor to the project associated with the issue.

    Methods:
        has_object_permission(request, view, obj): Check if the user has
            permission for the specified comment object.

    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission for the specified comment object.

        Args:
            request (Request): The request object.
            view (View): The view being accessed.
            obj: The object being accessed (in this case, a comment).

        Returns:
            bool: True if the user is the author of the associated issue or
            a contributor to the project, False otherwise.
        """
        if obj.issue.author == request.user:
            return True
        elif obj.issue.project.contributor.filter(pk=request.user.pk).exists():
            return True

from rest_framework import permissions

class IsIssueAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.issue.author == request.user:
            return True
        elif obj.issue.project.contributor.filter(pk=request.user.pk).exists():
            return True

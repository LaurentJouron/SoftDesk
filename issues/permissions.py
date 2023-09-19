from rest_framework import permissions

class IsProjectAuthorOrContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.project.author == request.user:
            return True
        elif obj.project.contributor.filter(pk=request.user.pk).exists():
            return True

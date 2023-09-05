# from rest_framework import permissions
# from .models import Project


# class CanDeleteAuthorProject(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method == "DELETE":
#             user = request.user
#             project_id = view.kwargs.get("pk")
#             if project.author == user:
#                 try:
#                     project = Project.objects.get(pk=project_id)
#                     return project.author == user
#                 except Project.DoesNotExist:
#                     return False
#             return True


# class CanViewProject(permissions.BasePermission):
#     def has_permission(self, request, view):
#         ...


# class CanEditProject(permissions.BasePermission):
#     def has_permission(self, request, view):
#         ...

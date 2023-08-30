from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

from .models import Issue


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        allowed_actions = ['create', 'list', 'retrieve']
        if view.action in allowed_actions:
            return True
        allowed_actions = ['update', 'destroy']
        if view.action in allowed_actions:
            issue = get_object_or_404(Issue, pk=view.kwargs['pk'])
            return request.user.is_author(issue)
        else:
            return False

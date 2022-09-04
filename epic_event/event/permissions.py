from rest_framework.permissions import BasePermission
from user.permissions import UserPermission


class EventPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ("list"):
            return True
        if view.action in ("update"):
            return UserPermission.is_support(request.user) or UserPermission.is_manager(
                request.user
            )
        if view.action in ("create"):
            return UserPermission.is_sales(request.user) or UserPermission.is_manager(
                request.user
            )
        return UserPermission.is_manager(request.user)

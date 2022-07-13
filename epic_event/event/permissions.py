from rest_framework.permissions import BasePermission
from user.permissions import UserTeam


class EventPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ("list"):
            return True
        if view.action in ("create", "update"):
            return UserTeam.is_support(request.user) or UserTeam.is_manager(
                request.user
            )
        if view.action in ("create"):
            return UserTeam.is_sales(request.user) or UserTeam.is_manager(request.user)
        return UserTeam.is_manager(request.user)

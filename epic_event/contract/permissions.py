from rest_framework.permissions import BasePermission
from user.models import User
from user.permissions import UserTeam


class ContractPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ("list"):
            return True
        if view.action in ("create", "update"):
            return UserTeam.is_sales(request.user) or UserTeam.is_manager(request.user)
        return UserTeam.is_manager(request.user)

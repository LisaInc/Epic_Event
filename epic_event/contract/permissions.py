from rest_framework.permissions import BasePermission
from user.permissions import UserPermission


class ContractPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ("list"):
            return True
        if view.action in ("create", "update"):
            return UserPermission.is_sales(request.user) or UserPermission.is_manager(
                request.user
            )
        return UserPermission.is_manager(request.user)

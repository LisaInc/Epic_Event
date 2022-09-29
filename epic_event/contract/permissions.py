from rest_framework.permissions import BasePermission
from user.permissions import CheckUserPermission


class ContractPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ("list"):
            return True
        if view.action in ("create", "update"):
            return CheckUserPermission.is_sales(
                request.user
            ) or CheckUserPermission.is_manager(request.user)
        return CheckUserPermission.is_manager(request.user)

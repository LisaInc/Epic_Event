from rest_framework.permissions import BasePermission


class UserPermission:
    def is_sales(user):
        return bool(user.groups.filter(name="sales"))

    def is_support(user):
        return bool(user.groups.filter(name="supports"))

    def is_manager(user):
        return bool(user.groups.filter(name="managers"))


class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == "list":
            return True
        if view.action in ("create", "update"):
            return UserPermission.is_sales(request.user) or UserPermission.is_manager(
                request.user
            )
        return UserPermission.is_manager(request.user)

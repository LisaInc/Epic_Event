from rest_framework.permissions import BasePermission


class CheckUserPermission:
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
            return CheckUserPermission.is_sales(
                request.user
            ) or CheckUserPermission.is_manager(request.user)
        return CheckUserPermission.is_manager(request.user)


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return CheckUserPermission.is_manager(request.user)

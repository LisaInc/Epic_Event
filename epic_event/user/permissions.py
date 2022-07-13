from rest_framework.permissions import BasePermission
from user.models import User
from user.permissions import UserTeam


class UserTeam:
    def is_sales(self, user):
        return bool(User.objects.filter(user=user, team="sales"))

    def is_support(self, user):
        return bool(User.objects.filter(user=user, team="support"))

    def is_manager(self, user):
        return bool(User.objects.filter(user=user, team="management"))


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return UserTeam.is_manager(request.user)


class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ("list"):
            return True
        if view.action in ("create", "update"):
            return UserTeam.is_sales(request.user) or UserTeam.is_manager(request.user)
        return UserTeam.is_manager(request.user)

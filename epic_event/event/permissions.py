from rest_framework.permissions import BasePermission
from user.permissions import CheckUserPermission
from event.models import Event


class EventPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ("list"):
            return True
        if view.action in ("update"):
            return Event.objects.filter(
                id=view.kwargs["pk"], support_contact=request.user
            ).exists() or CheckUserPermission.is_manager(request.user)
        if view.action in ("create"):
            return CheckUserPermission.is_sales(request.user) or CheckUserPermission.is_manager(
                request.user
            )
        return CheckUserPermission.is_manager(request.user)

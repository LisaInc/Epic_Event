from rest_framework.permissions import BasePermission
from user.permissions import UserPermission
from event.models import Event


class EventPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ("list"):
            return True
        if view.action in ("update"):
            print(
                Event.objects.filter(
                    id=view.kwargs["pk"], support_contact=request.user
                ).exists()
                or UserPermission.is_manager(request.user)
            )
            return Event.objects.filter(
                id=view.kwargs["pk"], support_contact=request.user
            ).exists() or UserPermission.is_manager(request.user)
        if view.action in ("create"):
            return UserPermission.is_support(request.user) or UserPermission.is_manager(
                request.user
            )
        return UserPermission.is_manager(request.user)

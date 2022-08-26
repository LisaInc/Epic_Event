from django.shortcuts import render
from rest_framework import viewsets
from event.models import Event
from event.serializers import EventSerializer
from rest_framework.viewsets import ModelViewSet
from user.permissions import UserPermission
from rest_framework.permissions import IsAuthenticated
from .permissions import EventPermission


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated, EventPermission]

    def has_permission(self, request, view):
        if view.action in ("list"):
            return True
        if view.action in ("create", "update"):
            return UserPermission.is_support(request.user) or UserPermission.is_manager(
                request.user
            )
        if view.action in ("create"):
            return UserPermission.is_sales(request.user) or UserPermission.is_manager(
                request.user
            )
        return UserPermission.is_manager(request.user)

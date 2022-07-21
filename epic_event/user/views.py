from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, generics
from user.permissions import UserPermission
from user.models import User, Client
from user.serializers import UserSerializer, ClientSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]
    queryset = User.objects.all()

    def has_permission(self, request, view):
        return UserPermission.is_manager(request.user)


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Client.objects.all()

    def has_permission(self, request, view):
        if view.action in ("list"):
            return True
        if view.action in ("create", "update"):
            return UserPermission.is_sales(request.user) or UserPermission.is_manager(
                request.user
            )
        return UserPermission.is_manager(request.user)

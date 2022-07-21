from django.shortcuts import render
from rest_framework import viewsets
from contract.models import Contract
from contract.serializers import ContractSerializer
from rest_framework.viewsets import ModelViewSet
from user.permissions import UserPermission
from rest_framework.permissions import IsAuthenticated


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Contract.objects.all()
    permission_classes = [IsAuthenticated]

    def has_permission(self, request, view):
        if view.action in ("list"):
            return True
        if view.action in ("create", "update"):
            return UserPermission.is_sales(request.user) or UserPermission.is_manager(
                request.user
            )
        return UserPermission.is_manager(request.user)

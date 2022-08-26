from django.shortcuts import render
from rest_framework import viewsets
from contract.models import Contract
from contract.serializers import ContractSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import ContractPermission


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Contract.objects.all()
    permission_classes = [IsAuthenticated, ContractPermission]

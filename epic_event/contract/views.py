from django.shortcuts import render
from rest_framework import viewsets
from contract.models import Contract
from contract.serializer import ContractSerializer
from rest_framework.viewsets import ModelViewSet

class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    # permission_classes = [ProjectPermissions]
    http_method_names = ["get", "post", "put", "delete"]

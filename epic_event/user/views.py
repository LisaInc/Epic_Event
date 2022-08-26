from django.shortcuts import render
from user.permissions import UserPermission, ClientPermission
from user.models import User, Client
from user.serializers import UserSerializer, ClientSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, ClientPermission]
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Client.objects.all()

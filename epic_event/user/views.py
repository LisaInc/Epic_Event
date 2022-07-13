from django.shortcuts import render
from rest_framework import viewsets
from user.models import User
from user.serializer import UserSerializer
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [ProjectPermissions]
    http_method_names = ["get", "post", "put", "delete"]

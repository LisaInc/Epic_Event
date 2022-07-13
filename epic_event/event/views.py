from django.shortcuts import render
from rest_framework import viewsets
from event.models import Event
from event.serializer import EventSerializer
from rest_framework.viewsets import ModelViewSet

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    # permission_classes = [ProjectPermissions]
    http_method_names = ["get", "post", "put", "delete"]
    
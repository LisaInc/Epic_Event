from rest_framework import serializers
from event.models import Event, EventStatus


class EventtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class EventStatustSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        fields = "__all__"

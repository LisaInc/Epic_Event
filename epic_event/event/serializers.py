from rest_framework import serializers
from event.models import Event, EventStatus
from user.serializers import UserSerializer, ClientSerializer
from user.models import User, Client


class EventStatustSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    support_contact = serializers.SlugRelatedField(
        queryset=User.objects.filter(groups__name="supports"), slug_field="username"
    )
    client = serializers.SlugRelatedField(
        queryset=Client.objects.all(), slug_field="company_name"
    )
    event_status = serializers.SlugRelatedField(
        queryset=EventStatus.objects.all(), slug_field="lib"
    )

    class Meta:
        model = Event
        fields = "__all__"

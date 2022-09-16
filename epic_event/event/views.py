from event.models import Event
from event.serializers import EventSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import EventPermission
from user.models import Client


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [IsAuthenticated, EventPermission]
    filterset_fields = (
        "client",
        "date_created",
        "date_update",
        "event_status",
        "attendees",
        "event_date",
        "notes",
        "support_contact",
    )

    def get_queryset(self):
        if self.request.user.groups.filter(name="supports"):
            return Event.objects.filter(support_contact=self.request.user)
        elif self.request.user.groups.filter(name="sales"):
            client = Client.objects.filter(sales_contact=self.request.user)
            return Event.objects.filter(client__in=client)

        return Event.objects.all()

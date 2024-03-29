from django.shortcuts import render
from user.permissions import ClientPermission, UserPermission
from user.models import User, Client
from user.serializers import UserSerializer, ClientSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from event.models import Event


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, ClientPermission]
    http_method_names = ["get", "post", "put", "delete"]
    filterset_fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "mobile",
        "company_name",
        "date_created",
        "date_update",
        "sales_contact",
    )

    def get_queryset(self):
        if self.request.user.groups.filter(name="sales"):
            return Client.objects.filter(
                Q(sales_contact=self.request.user) | Q(sales_contact__isnull=True)
            )
        elif self.request.user.groups.filter(name="supports"):
            client_id = [
                event.client.id
                for event in Event.objects.filter(support_contact=self.request.user)
            ]
            return Client.objects.filter(pk__in=client_id)
        return Client.objects.all()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, UserPermission]
    http_method_names = ["get", "post", "put", "delete"]
    queryset = User.objects.all()

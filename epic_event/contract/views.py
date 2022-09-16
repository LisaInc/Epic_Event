from contract.models import Contract
from contract.serializers import ContractSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import ContractPermission
from event.models import Event


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [IsAuthenticated, ContractPermission]
    filterset_fields = (
        "sale_contact",
        "client",
        "date_created",
        "date_update",
        "status",
        "amount",
        "payement_due",
    )

    def get_queryset(self):
        if self.request.user.groups.filter(name="supports"):
            client = [
                event.client
                for event in Event.objects.filter(support_contact=self.request.user)
            ]
            return Contract.objects.filter(client__in=client)
        elif self.request.user.groups.filter(name="sales"):
            return Contract.objects.filter(sale_contact=self.request.user)
        return Contract.objects.all()

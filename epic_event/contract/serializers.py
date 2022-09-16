from rest_framework import serializers
from contract.models import Contract
from user.models import User, Client


class ContractSerializer(serializers.ModelSerializer):
    sale_contact = serializers.SlugRelatedField(
        queryset=User.objects.filter(groups__name="sales"), slug_field="username"
    )
    client = serializers.SlugRelatedField(
        queryset=Client.objects.all(), slug_field="company_name"
    )

    class Meta:
        model = Contract
        fields = "__all__"

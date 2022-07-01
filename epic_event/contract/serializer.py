from rest_framework import serializers
from contract.models import Contract


class ContracttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"

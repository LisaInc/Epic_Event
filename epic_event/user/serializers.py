from django.contrib.auth.models import Group
from queue import Empty
from rest_framework import serializers
from user.models import User, Client


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        if validated_data["groups"]:
            user.groups.add(validated_data["groups"][0])
            if user.groups.get():
                user.is_staff = user.groups.get().name == "managers"
        user.save()
        return user


class ClientSerializer(serializers.ModelSerializer):
    sales_contact = serializers.SlugRelatedField(
        queryset=User.objects.filter(groups__name="sales"),
        slug_field="username",
        required=False,
    )

    class Meta:
        model = Client
        fields = "__all__"

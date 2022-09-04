from django.test import TestCase
from user.models import User
from user.serializers import UserSerializer
from django.contrib.auth.models import Group
import pytest


@pytest.mark.django_db
class UserTestCase(TestCase):
    def setUp(self):
        serializer = UserSerializer()
        manager_group = Group.objects.get(name="managers")
        support_group = Group.objects.get(name="supports")
        validated_data_manager = {
            "username": "test_manager",
            "password": "test",
            "email": "test@mail.com",
            "first_name": "test",
            "last_name": "test",
            "groups": [manager_group],
        }
        validated_data_support = {
            "username": "test_support",
            "password": "test",
            "email": "test@mail.com",
            "first_name": "test",
            "last_name": "test",
            "groups": [support_group],
        }
        serializer.create(validated_data_manager)
        serializer.create(validated_data_support)

    def test_create_user(self):
        test_manager = User.objects.get(username="test_manager")

        self.assertEqual(test_manager.username, "test_manager")
        self.assertEqual(test_manager.groups.get().name, "managers")
        self.assertEqual(test_manager.is_staff, True)

        test_support = User.objects.get(username="test_support")

        self.assertEqual(test_support.username, "test_support")
        self.assertEqual(test_support.groups.get().name, "supports")
        self.assertEqual(test_support.is_staff, False)

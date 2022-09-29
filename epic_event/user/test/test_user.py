from datetime import datetime, timezone
from django.test import TestCase
from user.models import User, Client
from django.contrib.auth.models import Group
import pytest


@pytest.mark.django_db
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test_manager", password="test")
        User.objects.create(username="test_support", password="test")
        Group.objects.create(name="manager")
        Group.objects.create(name="support")

    def test_create_user(self):
        test_manager = User.objects.get(username="test_manager")
        test_manager.groups.add(Group.objects.get(name="manager"))

        self.assertEqual(test_manager.username, "test_manager")
        self.assertEqual(test_manager.groups.get().name, "manager")

        test_support = User.objects.get(username="test_support")
        test_support.groups.add(Group.objects.get(name="support"))

        self.assertEqual(test_support.username, "test_support")
        self.assertEqual(test_support.groups.get().name, "support")


@pytest.mark.django_db
class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(
            first_name="test",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )

    def test_create_client(self):
        test_client = Client.objects.get(first_name="test")

        self.assertEqual(test_client.first_name, "test")
        self.assertEqual(test_client.last_name, "test")
        self.assertEqual(test_client.company_name, "company")

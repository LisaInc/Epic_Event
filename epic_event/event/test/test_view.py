from datetime import datetime, timezone
from django.test import TestCase
from django.test import Client as Cli
from event.models import Event, EventStatus
from user.models import User, Client
from django.contrib.auth.models import Group
import pytest
from user.models import User


@pytest.mark.django_db
class TestEvent(TestCase):
    client = Cli()

    def setUp(self):
        self.users = {}
        for user_group in ["manager", "sale", "support"]:
            user = User.objects.create(username=user_group)
            user.set_password("TestPassword")
            user.save()
            group = Group.objects.get(name=f"{user_group}s")
            user.groups.add(group)
            self.users[user_group] = user

    @pytest.mark.django_db
    def test_event(self):
        for user_group, user in self.users.items():
            user_data = {
                "username": user_group,
                "password": "TestPassword",
            }
            self.client.post("/login/", user_data)
            self.get_event()
            self.create_event(user)
            self.delete_event(user)
            self.change_event(user)

    def get_event(self):
        response = self.client.get("/event/")
        assert response.status_code == 200

    def create_event(self, user):
        event_status = EventStatus.objects.create(
            lib="test",
        )
        support_contact= User.objects.create(username=f"support_contact_{user.username}", password="test")
        print(User.objects.filter(username="support_contact_manager"))
        client_event = Client.objects.create(
            first_name=f"test_{user.username}",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )
        event = {
            "client": client_event.company_name,
            "date_update": datetime.now(tz=timezone.utc),
            "event_status": event_status.lib,
            "attendees": 100,
            "event_date": datetime.now(tz=timezone.utc),
            "notes": "test",

        }
        response = self.client.post("/event/", event)
        print(response.content)
        if user.username in ("manager", "sale"):
            assert response.status_code == 301
            assert Event.objects.filter(client=client_event).exists()
        else:
            assert response.status_code == 403
            assert Event.objects.filter(client=client_event).exists() == False

    def delete_event(self, user):
        event_status = EventStatus.objects.create(
            lib="test",
        )
        client_event = Client.objects.create(
            first_name=f"test{user.username}",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )
        event = Event.objects.create(
            client=client_event,
            date_update=datetime.now(tz=timezone.utc),
            event_status=event_status,
            attendees=100,
            event_date=datetime.now(tz=timezone.utc),
            notes="test",
        )
        response = self.client.delete(f"/event/{event.id}/")

        if user.username == "manager":
            assert Event.objects.filter(client=client_event).exists() == False
            assert response.status_code == 204
        else:
            assert response.status_code == 403
            assert Event.objects.filter(client=client_event).exists()

    def change_event(self, user):
        event_status = EventStatus.objects.create(
            lib="test",
        )
        client_event = Client.objects.create(
            first_name=f"test{user.username}",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )
        event = Event.objects.create(
            client=client_event,
            date_update=datetime.now(tz=timezone.utc),
            event_status=event_status,
            attendees=100,
            event_date=datetime.now(tz=timezone.utc),
            notes="test",
        )
        client_event_change = Client.objects.create(
            first_name=f"change{user.username}",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )
        event_change = {
            "client": client_event_change.id,
            "date_update": datetime.now(tz=timezone.utc),
            "event_status": event_status.id,
            "attendees": 100,
            "event_date": datetime.now(tz=timezone.utc),
            "notes": "test",
        }
        response = self.client.put(
            f"/event/{event.id}/",
            event_change,
            content_type="application/json",
        )

        if user.username in ("manager", "support"):
            assert response.status_code == 200
            assert Event.objects.filter(client=client_event_change).exists()
        else:
            assert response.status_code == 403
            assert Event.objects.filter(client=client_event).exists()

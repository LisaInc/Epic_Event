from django.test import TestCase
from event.models import Event, EventStatus
from user.models import Client
from datetime import datetime, timezone
import pytest


@pytest.mark.django_db
class EventStatusTestCase(TestCase):
    def setUp(self):
        EventStatus.objects.create(
            lib="test",
        )

    def test_create_event_status(self):
        event_status = EventStatus.objects.get(id=2)

        self.assertEqual(event_status.lib, "test")


@pytest.mark.django_db
class EventTestCase(TestCase):
    def setUp(self):
        event_status = EventStatus.objects.create(
            lib="test",
        )
        client = Client.objects.create(
            first_name="test",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )
        Event.objects.create(
            client=client,
            date_update=datetime.now(tz=timezone.utc),
            event_status=event_status,
            attendees=100,
            event_date=datetime.now(tz=timezone.utc),
            notes="test",
        )

    def test_create_event(self):
        for event in Event.objects.all():
            print(event.id)
        event = Event.objects.get(id=2)

        self.assertEqual(event.notes, "test")

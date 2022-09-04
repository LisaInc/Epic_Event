import pytest
from django.contrib import admin
from django.urls import resolve, reverse
from contract.models import Contract
from user.models import Client, User
from event.models import Event, EventStatus
from datetime import datetime, timezone


@pytest.mark.django_db
def test_client_url():
    user = User.objects.create(username="test", password="test")
    Client.objects.create(
        first_name="client_test",
        last_name="client_test",
        email="client_test@mail.com",
        mobile="client_test",
        date_update=datetime.now(tz=timezone.utc),
        company_name="client_test",
        sales_contact=user,
    )
    path = reverse("client-detail", kwargs={"pk": 1})

    assert resolve(path).view_name == "client-detail"
    assert path == "/client/1/"


@pytest.mark.django_db
def test_contract_url():
    user = User.objects.create(username="test", password="test")
    client = Client.objects.create(
        first_name="client_test",
        last_name="client_test",
        email="client_test@mail.com",
        mobile="client_test",
        date_update=datetime.now(tz=timezone.utc),
        company_name="client_test",
        sales_contact=user,
    )
    Contract.objects.create(
        sale_contact=user,
        client=client,
        date_created=datetime.now(tz=timezone.utc),
        date_update=datetime.now(tz=timezone.utc),
        status=True,
        amount=100,
        payement_due=datetime.now(tz=timezone.utc),
    )
    path = reverse("contract-detail", kwargs={"pk": 1})

    assert resolve(path).view_name == "contract-detail"
    assert path == "/contract/1/"


@pytest.mark.django_db
def test_event_url():
    user = User.objects.create(username="test", password="test")
    client = Client.objects.create(
        first_name="client_test",
        last_name="client_test",
        email="client_test@mail.com",
        mobile="client_test",
        date_update=datetime.now(tz=timezone.utc),
        company_name="client_test",
        sales_contact=user,
    )
    status = EventStatus.objects.create(lib="En cours")
    Event.objects.create(
        client=client,
        date_created=datetime.now(tz=timezone.utc),
        date_update=datetime.now(tz=timezone.utc),
        event_status=status,
        attendees=4,
        event_date=datetime.now(tz=timezone.utc),
        notes="notes",
        support_contact=user,
    )
    path = reverse("event-detail", kwargs={"pk": 1})

    assert resolve(path).view_name == "event-detail"
    assert path == "/event/1/"

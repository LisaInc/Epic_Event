from django.test import TestCase
from contract.models import Contract
from user.models import Client, User
from datetime import datetime, timezone
import pytest


@pytest.mark.django_db
class ContractStatusTestCase(TestCase):
    def setUp(self):
        client = Client.objects.create(
            first_name="test",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )
        sale_contact = User.objects.create(username="sale", password="test")
        Contract.objects.create(
            sale_contact=sale_contact,
            client=client,
            date_created=datetime.now(tz=timezone.utc),
            date_update=datetime.now(tz=timezone.utc),
            status=1,
            amount=1000,
            payement_due=datetime.now(tz=timezone.utc),
        )

    def test_create_contract(self):
        contract = Contract.objects.get(id=1)
        client = Client.objects.get(first_name="test")
        self.assertEqual(contract.client, client)

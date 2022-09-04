from datetime import datetime, timezone
from django.test import TestCase
from django.test import Client as Cli
from contract.models import Contract
from user.models import User, Client
from django.contrib.auth.models import Group
import pytest
from user.models import User


@pytest.mark.django_db
class TestContract(TestCase):
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
    def test_contract(self):
        for user_group, user in self.users.items():
            user_data = {
                "username": user_group,
                "password": "TestPassword",
            }
            self.client.post("/login/", user_data)
            self.get_contract()
            self.create_contract(user)
            self.delete_contract(user)
            self.change_contract(user)

    def get_contract(self):
        response = self.client.get("/contract/")
        assert response.status_code == 200

    def create_contract(self, user):
        client_contract = Client.objects.create(
            first_name="test",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )
        sale_contact = User.objects.create(
            username=f"create_sales_{user.username}", password="test"
        )
        contract_create = {
            "sale_contact": sale_contact.id,
            "client": client_contract.id,
            "date_created": datetime.now(tz=timezone.utc),
            "date_update": datetime.now(tz=timezone.utc),
            "status": 1,
            "amount": 1000,
            "payement_due": datetime.now(tz=timezone.utc),
        }
        response = self.client.post(f"/contract/", contract_create)

        if user.username in ("manager", "sale"):
            assert Contract.objects.filter(sale_contact=sale_contact).exists()
            assert response.status_code == 201
        else:
            assert response.status_code == 403
            assert Contract.objects.filter(sale_contact=sale_contact).exists() == False

    def delete_contract(self, user):
        client_contract = Client.objects.create(
            first_name="test",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )
        sale_contact = User.objects.create(
            username=f"sale_contract{user.username}", password="test"
        )
        contract = Contract.objects.create(
            sale_contact=sale_contact,
            client=client_contract,
            date_created=datetime.now(tz=timezone.utc),
            date_update=datetime.now(tz=timezone.utc),
            status=1,
            amount=1000,
            payement_due=datetime.now(tz=timezone.utc),
        )
        response = self.client.delete(f"/contract/{contract.id}/")

        if user.username == "manager":
            assert Contract.objects.filter(sale_contact=sale_contact).exists() == False
            assert response.status_code == 204
        else:
            assert response.status_code == 403
            assert Contract.objects.filter(sale_contact=sale_contact).exists()

    def change_contract(self, user):
        client_contract = Client.objects.create(
            first_name="test",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )
        sale_contact = User.objects.create(
            username=f"to_change_sales_{user.username}", password="test"
        )
        changed_sales = User.objects.create(
            username=f"changed_sale{user.username}", password="test"
        )
        contract = Contract.objects.create(
            sale_contact=sale_contact,
            client=client_contract,
            date_created=datetime.now(tz=timezone.utc),
            date_update=datetime.now(tz=timezone.utc),
            status=1,
            amount=1000,
            payement_due=datetime.now(tz=timezone.utc),
        )
        contract_changes = {
            "id": contract.id,
            "sale_contact": changed_sales.id,
            "client": client_contract.id,
            "date_created": datetime.now(tz=timezone.utc),
            "date_update": datetime.now(tz=timezone.utc),
            "status": 1,
            "amount": 1000,
            "payement_due": datetime.now(tz=timezone.utc),
        }
        response = self.client.put(
            f"/contract/{contract.id}/",
            contract_changes,
            content_type="application/json",
        )

        if user.username in ("manager", "sale"):
            assert response.status_code == 200
            assert Contract.objects.filter(sale_contact=changed_sales).exists()
        else:
            assert response.status_code == 403
            assert Contract.objects.filter(sale_contact=sale_contact).exists()

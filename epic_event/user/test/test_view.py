from datetime import datetime, timezone
from django.test import TestCase
from django.test import Client as Cli
from django.test import TestCase
from user.models import User, Client
from django.contrib.auth.models import Group
import pytest
from user.models import User


@pytest.mark.django_db
class TestUsers(TestCase):
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
    def test_login_valid(self):
        user_data = {
            "username": "manager",
            "password": "TestPassword",
        }
        response = self.client.post("/login/", user_data)

        assert response.url == "/"
        assert response.status_code == 302
        assert response.wsgi_request.user.username == "manager"

    @pytest.mark.django_db
    def test_login_invalid(self):
        user_data = {
            "username": "test",
            "password": "wrong",
        }
        response = self.client.post("/login/", user_data)

        assert b"Please enter a correct username and password." in response.content
        assert response.status_code == 200
        assert response.wsgi_request.user.__str__() == "AnonymousUser"

    @pytest.mark.django_db
    def test_logout_user(self):
        response = self.client.post("/logout/")

        assert response.wsgi_request.user.__str__() == "AnonymousUser"

    @pytest.mark.django_db
    def test_client(self):
        for user_group, user in self.users.items():
            user_data = {
                "username": user_group,
                "password": "TestPassword",
            }
            self.client.post("/login/", user_data)
            self.get_client()
            self.create_client(user)
            self.delete_client(user)
            self.change_client(user)

    def get_client(self):
        response = self.client.get("/client/")
        assert response.status_code == 200

    def create_client(self, user):
        client_create = {
            "first_name": f"create_{user.username}",
            "last_name": "test",
            "email": "test@mail.com",
            "mobile": "0000000000",
            "company_name": "company",
            "date_update": datetime.now(tz=timezone.utc),
        }
        response = self.client.post(f"/client/", client_create)

        if user.username in ("manager", "sale"):
            assert Client.objects.filter(first_name=f"create_{user.username}").exists()
            assert response.status_code == 201
        else:
            assert response.status_code == 403
            assert (
                Client.objects.filter(first_name=f"create_{user.username}").exists()
                == False
            )

    def delete_client(self, user):
        client_delete = Client.objects.create(
            first_name="test",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )
        response = self.client.delete(f"/client/{client_delete.id}/")

        if user.username == "manager":
            assert Client.objects.filter(id=client_delete.id).exists() == False
            assert response.status_code == 204
        else:
            assert response.status_code == 403
            assert Client.objects.filter(id=client_delete.id).exists()

    def change_client(self, user):
        client_to_change = Client.objects.create(
            first_name=f"to_change_{user.username}",
            last_name="test",
            email="test@mail.com",
            mobile="0000000000",
            company_name="company",
            date_update=datetime.now(tz=timezone.utc),
        )
        client_changes = {
            "id": client_to_change.id,
            "first_name": f"changed_{user.username}",
            "last_name": "test",
            "email": "test@mail.com",
            "mobile": "0000000000",
            "company_name": "company",
            "date_update": datetime.now(tz=timezone.utc),
        }
        response = self.client.put(
            f"/client/{client_to_change.id}/",
            client_changes,
            content_type="application/json",
        )

        if user.username in ("manager", "sale"):
            assert response.status_code == 200
            assert Client.objects.filter(first_name=f"changed_{user.username}").exists()
        else:
            assert response.status_code == 403
            assert Client.objects.filter(
                first_name=f"to_change_{user.username}"
            ).exists()

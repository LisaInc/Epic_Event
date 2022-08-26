from django.contrib.auth.models import User
from django.test import TestCase, Client
from models import User


class TestOrganizationViewSet(TestCase):
    url = "/organizations/"

    def create_user(self, is_admin):
        password = "password"

        user = User.objects.create()
        user.set_password(password)
        user.save()

        return user, password

    def get_organizations_as(self, user=None, password=None):
        api = Client()

        if user:
            mommy.make(Membership, user=user, organization=mommy.make(Organization))
            api.login(username=user.username, password=password)

        return api.get(self.url)

    def test_organizations_viewset_returns_200_for_admins(self):
        response = self.get_organizations_as(*self.create_user(True))
        self.assertEqual(response.status_code, 200)

    def test_organizations_viewset_returns_403_for_non_admins(self):
        response = self.get_organizations_as(*self.create_user(False))
        self.assertEqual(response.status_code, 403)

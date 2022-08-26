from django.test import TestCase
from user.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test", password="test")
        User.objects.create(username="test1", password="test")

    def test_animals_can_speak(self):
        """Users that can speak are correctly identified"""
        lion = User.objects.get(username="test")
        # lion.groups.set()
        # cat = User.objects.get(name="test1")
        self.assertEqual(lion.username, "test")
        # self.assertEqual(cat.speak(), 'The cat says "meow"')

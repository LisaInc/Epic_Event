from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    team_choice = [
        ("sales", "sales"),
        ("support", "support"),
        ("management", "management"),
    ]
    team = models.CharField(choices=team_choice, max_length=25, blank=True)
    if team == "management":
        is_staff = True
    else:
        is_staff = False


class Client(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField()
    sales_contact = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)

from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    pass


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(blank=True, max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField()
    sales_contact = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.company_name}"

from django.db import models
from user.models import User, Client


class Contract(models.Model):
    sale_contact = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField()
    status = models.BooleanField()
    amount = models.FloatField()
    payement_due = models.DateTimeField()

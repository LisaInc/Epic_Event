from typing_extensions import Required
from django.db import models
from user.models import Client, User


class EventStatus(models.Model):
    lib = models.TextField()

    def __str__(self) -> str:
        return self.lib


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField()
    event_status = models.ForeignKey(to=EventStatus, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.CharField(max_length=500)
    support_contact = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True, default='')

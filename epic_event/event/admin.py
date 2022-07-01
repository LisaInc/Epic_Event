from django.contrib import admin
from event.models import Event, EventStatus

admin.site.register(Event)
admin.site.register(EventStatus)

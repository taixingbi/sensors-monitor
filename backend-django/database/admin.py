from django.contrib import admin

from .models import Sensor
from .models import Heartbeat

admin.site.register(Sensor)
admin.site.register(Heartbeat)


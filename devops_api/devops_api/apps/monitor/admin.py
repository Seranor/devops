from django.contrib import admin

from .models import MonitorHost, MonitorParams

admin.site.register(MonitorHost)
admin.site.register(MonitorParams)

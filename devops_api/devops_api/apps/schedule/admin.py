from django.contrib import admin

from .models import TaskSchedule, TaskHost

admin.site.register(TaskSchedule)
admin.site.register(TaskHost)

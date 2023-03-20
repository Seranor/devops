from django.contrib import admin

from .models import CmdTemplateCategory, CmdTemplate

admin.site.register(CmdTemplate)
admin.site.register(CmdTemplateCategory)

from django.contrib import admin

from .models import Host, HostCategory, PkeyModel

admin.site.register(Host)
admin.site.register(HostCategory)
admin.site.register(PkeyModel)

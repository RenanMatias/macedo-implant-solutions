from django.contrib import admin

from .models.client import Client


class ClientAdmin(admin.ModelAdmin):
    ...


admin.site.register(Client, ClientAdmin)

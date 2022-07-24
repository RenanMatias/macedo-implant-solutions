from django.contrib import admin

from .models.client import Client
from .models.order import Order


class ClientAdmin(admin.ModelAdmin):
    ...


class OrderAdmin(admin.ModelAdmin):
    ...


admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)

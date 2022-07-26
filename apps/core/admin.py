from django.contrib import admin

from .models import Client, Material, Order, Sales


class ClientAdmin(admin.ModelAdmin):
    ...


class OrderAdmin(admin.ModelAdmin):
    ...


class MaterialAdmin(admin.ModelAdmin):
    ...


class SalesAdmin(admin.ModelAdmin):
    ...


admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Material, OrderAdmin)
admin.site.register(Sales, SalesAdmin)

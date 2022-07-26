from django.contrib import admin

from .models import Client, Material, Order, Sale, Stock


class ClientAdmin(admin.ModelAdmin):
    ...


class OrderAdmin(admin.ModelAdmin):
    ...


class MaterialAdmin(admin.ModelAdmin):
    ...


class SaleAdmin(admin.ModelAdmin):
    ...


class StockAdmin(admin.ModelAdmin):
    ...


admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Material, OrderAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Stock, StockAdmin)

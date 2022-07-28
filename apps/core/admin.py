from django.contrib import admin

from .models import (Bank, Billing, Client, Material, Order, Payment, Sale,
                     Stock)


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


class BillingAdmin(admin.ModelAdmin):
    ...


class BankAdmin(admin.ModelAdmin):
    ...


class PaymentAdmin(admin.ModelAdmin):
    ...


admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Material, OrderAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Billing, BillingAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Payment, PaymentAdmin)

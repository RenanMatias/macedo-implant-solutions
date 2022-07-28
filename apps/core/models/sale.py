from django.db import models

from .material import Material
from .order import Order


class Sale(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order.id)

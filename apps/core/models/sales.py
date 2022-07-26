from django.db import models

from .material import Material
from .order import Order


class Sales(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return str(self.id)

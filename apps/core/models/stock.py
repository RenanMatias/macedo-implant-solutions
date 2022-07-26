from django.db import models

from .material import Material


class Stock(models.Model):
    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT
    )
    lote = models.CharField(max_length=255, null=True, blank=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return str(self.material.codigo)

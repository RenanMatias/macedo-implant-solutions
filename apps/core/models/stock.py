from django.db import models

from .material import Material


class Stock(models.Model):
    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT
    )
    lote = models.CharField(max_length=255, null=True, blank=True)
    quantidade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.material.codigo)

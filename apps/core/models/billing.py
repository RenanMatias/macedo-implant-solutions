from django.db import models

from .sale import Sale


class Billing(models.Model):
    STATUS_CHOICES = (
        ('Aberto', 'Aberto'),
        ('Fechado', 'Fechado'),
        ('Cancelado', 'Cancelado'),
    )
    venda = models.ForeignKey(
        Sale,
        on_delete=models.PROTECT
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='Aberto',
        max_length=50
    )
    total_parcela = models.CharField(max_length=255, null=True, blank=True)
    desconto = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        default=0
    )
    tipo_frete = models.CharField(max_length=255, null=True, blank=True)
    valor_frete = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

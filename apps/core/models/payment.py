from django.db import models

from .billing import Billing


class Payment(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='Pendente',
        max_length=50
    )
    faturamento = models.ForeignKey(
        Billing,
        on_delete=models.PROTECT
    )
    forma_pagamento = models.CharField(max_length=255)
    observacao = models.TextField(null=True, blank=True)
    parcela = models.CharField(max_length=255, null=True, blank=True)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

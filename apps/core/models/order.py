from django.db import models

from apps.users.models import User

from .client import Client


class Order(models.Model):
    STATUS_CHOICES = (
        ('Aberto', 'Aberto'),
        ('Fechado', 'Fechado'),
        ('Cancelado', 'Cancelado'),
    )

    # Fields
    username = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    data_pedido = models.DateField(auto_now_add=True)
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='Aberto',
        max_length=50
    )
    dentista = models.CharField(max_length=255, null=True, blank=True)
    instituicao = models.CharField(max_length=255, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

from django.db import models

from apps.users.models import User


class Material(models.Model):
    STATUS_CHOICES = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    )
    # Fields
    codigo = models.CharField(max_length=255, unique=True)
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='Ativo',
        max_length=50
    )
    descricao = models.CharField(max_length=255)
    tamanho = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    plataforma = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    username = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codigo

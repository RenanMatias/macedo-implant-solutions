from django.db import models

from apps.users.models import User

# Create your models here.


class Client(models.Model):
    TIPO_CHOICES = (
        ('Dentista', 'Dentista'),
        ('Paciente', 'Paciente'),
        ('Instituição', 'Instituição')
    )
    STATUS_CHOICES = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    )

    tipo = models.CharField(
        choices=TIPO_CHOICES,
        max_length=50
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='Ativo',
        max_length=50
    )
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    cro_uf = models.CharField(max_length=50)
    cro = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    desconto = models.DecimalField(decimal_places=2, default=0, max_digits=5)
    data_aniversario = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

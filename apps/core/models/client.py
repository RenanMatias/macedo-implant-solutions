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

    # Fields
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
    cpf = models.CharField(max_length=255, null=True, blank=True, unique=True)
    cnpj = models.CharField(max_length=255, null=True, blank=True, unique=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=255, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    municipio = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    uf = models.CharField(max_length=255, null=True, blank=True)
    cep = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    celular = models.CharField(max_length=255, null=True, blank=True)
    cro_uf = models.CharField(max_length=255, null=True, blank=True)
    cro = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    desconto = models.DecimalField(
        decimal_places=0,
        default=0,
        max_digits=3
    )
    data_aniversario = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nome

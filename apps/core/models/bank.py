from django.db import models


class Bank(models.Model):
    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=255)
    agencia = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

from django.test import TestCase

from apps.core.models.client import Client
from apps.users.models import User
from utils.factory import make_client as mc


class ClientTestBase(TestCase):
    def make_user(self, username='test_user', password='test_password'):
 
        user = User.objects.create_user(
            username=username,
            password=password
        )

        self.client.login(
            username='test_user',
            password='test_password'
        )

        return user

    def make_client(self, username_data, tipo=None, status=None, nome=None, cpf=None, cnpj=None):

        client = mc(tipo=tipo, status=status, nome=nome, cpf=cpf, cnpj=cnpj)

        return Client.objects.create(
            tipo=client['tipo'],
            status=client['status'],
            nome=client['nome'],
            cpf=client['cpf'],
            cnpj=client['cnpj'],
            username=username_data
        )

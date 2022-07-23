from django.test import TestCase

from apps.core.models import Client
from apps.users.models import User


class CoreMixing:
    def make_user(self,
                  first_name='user',
                  last_name='name',
                  username='username',
                  password='123456',
                  email='username@email.com'
                  ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_client(self,
                    tipo='Dentista',
                    status='Ativo',
                    nome='Lívia Evelyn Gomes',
                    cpf='32144043930',
                    cnpj='29365802000187',
                    endereco='Avenida Gonçalo Rolemberg Leite',
                    numero='331',
                    complemento='Casa 1',
                    bairro='Luzia',
                    municipio='Aracaju',
                    cidade='Aracaju',
                    uf='SE',
                    cep='49045280',
                    telefone='7938150114',
                    celular='79994084101',
                    cro_uf='CRO-SE',
                    cro='123456',
                    email='liviaevelyngomes@zulix.com.br',
                    desconto=0.0,
                    data_aniversario='2022-01-01',
                    username=None
                    ):
        return Client.objects.create(
            tipo=tipo,
            status=status,
            cpf=cpf,
            nome=nome,
            cnpj=cnpj,
            endereco=endereco,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            municipio=municipio,
            cidade=cidade,
            uf=uf,
            cep=cep,
            telefone=telefone,
            celular=celular,
            cro_uf=cro_uf,
            cro=cro,
            email=email,
            desconto=desconto,
            data_aniversario=data_aniversario,
            username=username
        )


class CoreTestBase(TestCase, CoreMixing):
    def setUp(self) -> None:
        return super().setUp()

from django.test import TestCase

from apps.core.models import (Bank, Billing, Client, Material, Order, Payment,
                              Sale, Stock)
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

    def make_order(self,
                   username=None,
                   data_pedido='2020-01-01',
                   client=None,
                   status='Aberto',
                   dentista='Dentista',
                   instituicao='Instituição',
                   observacao='Observação',
                   ):
        return Order.objects.create(
            username=username,
            data_pedido=data_pedido,
            client=client,
            status=status,
            dentista=dentista,
            instituicao=instituicao,
            observacao=observacao,
        )

    def make_material(self,
                      codigo='123456',
                      status='Ativo',
                      descricao='Descrição',
                      tamanho='Tamanho',
                      marca='Marca',
                      modelo='Modelo',
                      plataforma='Plataforma',
                      local='Local',
                      custo=0.0,
                      valor_unitario=0.0,
                      username=None
                      ):
        return Material.objects.create(
            codigo=codigo,
            status=status,
            descricao=descricao,
            tamanho=tamanho,
            marca=marca,
            modelo=modelo,
            plataforma=plataforma,
            local=local,
            custo=custo,
            valor_unitario=valor_unitario,
            username=username
        )

    def make_bank(self, codigo='1', nome='Banco Teste', agencia='1', conta='1'):
        return Bank.objects.create(
            codigo=codigo,
            nome=nome,
            agencia=agencia,
            conta=conta,
        )

    def make_stock(self,
                   material=None,
                   lote='1',
                   quantidade=0,
                   ):
        return Stock.objects.create(
            material=material,
            lote=lote,
            quantidade=quantidade
        )

    def make_sale(self,
                  order=None,
                  material=None,
                  ):
        return Sale.objects.create(
            order=order,
            material=material,
        )

    def make_billing(self,
                     venda=None,
                     total_parcela='1',
                     desconto=1.0,
                     tipo_frete='frete',
                     valor_frete=1.0,
                     valor_total=1.0,
                     ):
        return Billing.objects.create(
            venda=venda,
            total_parcela=total_parcela,
            desconto=desconto,
            tipo_frete=tipo_frete,
            valor_frete=valor_frete,
            valor_total=valor_total,
        )

    def make_payment(self,
                     faturamento=None,
                     forma_pagamento='Dinheiro',
                     observacao='Observação',
                     parcela='1',
                     data_vencimento='2020-01-01',
                     data_pagamento='2020-01-01',
                     valor=1.0,
                     ):
        return Payment.objects.create(
            faturamento=faturamento,
            forma_pagamento=forma_pagamento,
            observacao=observacao,
            parcela=parcela,
            data_vencimento=data_vencimento,
            data_pagamento=data_pagamento,
            valor=valor,
        )


class CoreTestBase(TestCase, CoreMixing):
    def setUp(self) -> None:
        return super().setUp()

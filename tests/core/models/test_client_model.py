from django.core.exceptions import ValidationError
from parameterized import parameterized

from tests.core.models.test_core_models_base import CoreTestBase
from utils.cpf_cnpj_validation import cnpj_validate, cpf_validate


class ClientModelTest(CoreTestBase):
    def setUp(self) -> None:
        return super().setUp()

    @parameterized.expand([
        ('nome', 255),
        ('cpf', 11),
        ('cnpj', 14),
        ('endereco', 255),
        ('numero', 10),
        ('complemento', 255),
        ('bairro', 255),
        ('municipio', 255),
        ('cidade', 255),
        ('uf', 2),
        ('cep', 10),
        ('telefone', 15),
        ('celular', 15),
        ('cro_uf', 50),
        ('cro', 50),
    ])
    def test_client_text_fields_max_length(self, field, max_length):
        client = self.make_client(
            username=self.make_user()
        )
        setattr(client, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            client.full_clean()

    def test_client_different_client_type_from_list(self):
        client = self.make_client(
            tipo='Anestesista',
            username=self.make_user()
        )
        with self.assertRaises(ValidationError):
            client.full_clean()

    def test_client_different_status_from_list(self):
        client = self.make_client(
            status='Desligado',
            username=self.make_user()
        )
        with self.assertRaises(ValidationError):
            client.full_clean()

    @parameterized.expand([
        '20921238070',
        '799.959.230-76'
    ])
    def test_client_CPF_validation(self, cpf):
        self.assertTrue(cpf_validate(cpf))

    @parameterized.expand([
        '55551065000117',
        '92.515.869/0001-97',
    ])
    def test_client_CNPJ_validation(self, cnpj):
        self.assertTrue(cnpj_validate(cnpj))

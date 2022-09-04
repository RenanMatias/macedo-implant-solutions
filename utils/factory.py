# cspell:skip
# cspell:ignore-line
# cspell:ignore-next
# cspell:ignore
from random import choice, randint

from faker import Faker  # https://faker.readthedocs.io/en/master/index.html

fake = Faker('pt_BR')
tipo = ['Dentista', 'Paciente', 'Instituição']
status = ['Ativo', 'Inativo']


# cSpell:disable
def make_client() -> dict:
    uf = fake.estado_sigla()
    return {
        'tipo': choice(tipo),
        'status': choice(status),
        'nome': fake.name(),
        'cpf': fake.ssn(),
        'cnpj': fake.company_id(),
        'endereco': f'{fake.street_prefix()} {fake.street_name()}',
        'numero': fake.building_number(),
        'complemento': '-',
        'bairro': fake.bairro(),
        'municipio': fake.neighborhood(),
        'cidade': fake.city(),
        'cep': fake.postcode(formatted=False),
        'uf': uf,
        'telefone': fake.msisdn(),
        'celular': fake.msisdn(),
        'cro_uf': uf,
        'cro': randint(10000, 99999),
        'email': fake.ascii_safe_email(),
        'desconto': 0,
        'data_aniversario': fake.date(end_datetime='-20y')
    }
# cSpell:enable


# if __name__ == '__main__':
#     from pprint import pprint
#     pprint(make_client())

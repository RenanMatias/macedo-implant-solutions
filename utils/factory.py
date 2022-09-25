from random import choice, randint

from faker import Faker  # https://faker.readthedocs.io/en/master/index.html

fake = Faker('pt_BR')
tipo_choice = ['Dentista', 'Paciente', 'Instituição']
status_choice = ['Ativo', 'Inativo']


# cSpell:disable
def make_client(tipo=None, status=None, nome=None, cpf=None, cnpj=None) -> dict:

    tipo1 = choice(tipo_choice) if tipo is None else tipo
    status1 = choice(status_choice) if status is None else status
    nome1 = fake.name() if nome is None else nome
    cpf1 = fake.ssn() if cpf is None else cpf
    cnpj1 = fake.company_id() if cnpj is None else cnpj

    uf = fake.estado_sigla()
    return {
        'tipo': tipo1,
        'status': status1,
        'nome': nome1,
        'cpf': cpf1,
        'cnpj': cnpj1,
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

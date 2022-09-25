from django import forms

from utils.django_forms import add_attr, add_placeholder, override_attr

from ..models.client import Client

UF_CHOICES = (
    ('', ''),
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AM', 'AM'),
    ('AP', 'AP'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MG', 'MG'),
    ('MS', 'MS'),
    ('MT', 'MT'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('PR', 'PR'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('RS', 'RS'),
    ('SC', 'SC'),
    ('SE', 'SE'),
    ('SP', 'SP'),
    ('TO', 'TO')
)


class DateInput(forms.DateInput):
    input_type = 'date'


class ClientForm(forms.ModelForm):
    uf = forms.ChoiceField(
        choices=UF_CHOICES,
        label='UF',
        required=False
    )
    cro_uf = forms.ChoiceField(
        choices=UF_CHOICES,
        label='CRO-UF',
        required=False
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Class
        add_attr(self.fields.get('tipo'), 'class', 'col-start-1 col-end-2')
        add_attr(self.fields.get('nome'), 'class', 'col-start-1 col-span-2')
        
        # Placeholder
        add_placeholder(self.fields.get('telefone'), '21 1234-5678')
        add_placeholder(self.fields.get('celular'), '21 12345-6789')

        # Maxlength
        override_attr(self.fields.get('cpf'), 'maxlength', '14')
        override_attr(self.fields.get('cnpj'), 'maxlength', '19')
        override_attr(self.fields.get('cep'), 'maxlength', '9')
        override_attr(self.fields.get('telefone'), 'maxlength', '12')
        override_attr(self.fields.get('celular'), 'maxlength', '13')
        
    class Meta:
        model = Client
        fields = [
            'tipo',
            'nome',
            'cpf',
            'cnpj',
            'email',
            'cep',
            'endereco',
            'numero',
            'complemento',
            'bairro',
            'municipio',
            'cidade',
            'uf',
            'telefone',
            'celular',
            'cro_uf',
            'cro',
            'desconto',
            'data_aniversario'
        ]
        labels = {
            'cpf': 'CPF',
            'cnpj': 'CNPJ',
            'endereco': 'Endereço',
            'cep': 'CEP',
            'numero': 'Número',
            'municipio': 'Município',
            'cro': 'Número CRO',
            'desconto': 'Desconto (%)'
        }
        widgets = {
            'data_aniversario': DateInput()
        }

from django import forms

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


class ClientForm(forms.ModelForm):
    cpf = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'maxlength': 14
            }
        ),
        label='CPF',
        required=False
    )
    cnpj = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'maxlength': 19
            }
        ),
        label='CNPJ',
        required=False
    )
    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'maxlength': 9,
                'class': 'col-start-1 col-end-2'
            }
        ),
        label='CEP',
        required=False
    )
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

    class Meta:
        model = Client
        fields = [
            'tipo',
            'nome',
            'cpf',
            'cnpj',
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
            'email',
            'desconto',
            'data_aniversario'
        ]
        labels = {
            'endereco': 'Endereço',
            'numero': 'Número',
            'municipio': 'Município',
            'cro': 'Número CRO',
            'desconto': 'Desconto (%)',
            'data_aniversario': 'Data de Aniversário'
        }
        widgets = {
            'tipo': forms.Select(
                attrs={
                    'class': 'col-start-1 col-end-2',
                }
            ),
            'nome': forms.TextInput(
                attrs={
                    'class': 'col-start-1 col-span-2',
                }
            )
        }

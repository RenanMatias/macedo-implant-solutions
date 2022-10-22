from django import forms
from django.core.exceptions import ValidationError

from utils.cpf_cnpj_validation import cnpj_validate, cpf_validate
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
    cro_uf = forms.ChoiceField(
        choices=UF_CHOICES,
        label='CRO-UF',
        required=False
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Class
        fieldsToClass = (
            ('tipo', 'col-start-1 col-end-2'),
            ('nome', 'col-start-1 col-span-2'),
        )
        for field, attr in fieldsToClass:
            add_attr(self.fields.get(field), 'class', attr)
        
        # Placeholder
        fieldsToPlaceholder = (
            ('telefone', '21 1234-5678'),
            ('celular', '21 12345-6789'),
        )
        for field, placeholder in fieldsToPlaceholder:
            add_placeholder(self.fields.get(field), placeholder)

        # Maxlength
        fieldsToMaxlength = (
            ('cpf', '14'),
            ('cnpj', '19'),
            ('cep', '9'),
            ('telefone', '12'),
            ('celular', '13'),
        )
        for field, maxlength in fieldsToMaxlength:
            override_attr(self.fields.get(field), 'maxlength', maxlength)

        # Readonly Fields
        fieldsToReadonly = ('endereco', 'bairro', 'cidade', 'uf')
        for field in fieldsToReadonly:
            add_attr(self.fields.get(field), 'readonly')
        
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
            'desconto': 'Desconto (%)',
            'uf': 'UF'
        }
        widgets = {
            'data_aniversario': DateInput()
        }

    def clean(self):
        cleaned_data = super().clean()

        tipo = cleaned_data.get('tipo')
        cpf = cleaned_data.get('cpf')
        cnpj = cleaned_data.get('cnpj')
        cro_uf = cleaned_data.get('cro_uf')
        cro = cleaned_data.get('cro')
        cep = cleaned_data.get('cep')
        endereco = (cleaned_data.get('endereco'))
        numero = cleaned_data.get('numero')

        errors = []

        if tipo == 'Dentista':
            if cpf is None and cnpj is None:
                errors += [('cpf', 'Informe o CPF ou o CNPJ.')]
                errors += [('cnpj', 'Informe o CPF ou o CNPJ.')]
            if cro_uf == '':
                errors += [('cro_uf', 'Campo Obrigatório')]
            if cro is None:
                errors += [('cro', 'Campo Obrigatório')]

        elif tipo == 'Paciente':
            if cpf is None:
                errors += [('cpf', 'Campo Obrigatório')]

        if tipo == 'Dentista' or tipo == 'Paciente':
            if cep is None:
                errors += [('cep', 'Campo Obrigatório')]
            if cep is not None and endereco is None:
                errors += [('cep', 'CEP inválido')]
            if numero is None:
                errors += [('numero', 'Campo Obrigatório')]
        
        if cpf is not None and not cpf_validate(cpf):
            errors += [('cpf', 'CPF inválido, verifique os números digitados.')]
        if cnpj is not None and not cnpj_validate(cnpj):
            errors += [('cnpj', 'CNPJ inválido, verifique os números digitados.')]
                
        validarionErrors = {}
        for field, message in errors:
            validarionErrors[field] = message

        raise ValidationError(validarionErrors)

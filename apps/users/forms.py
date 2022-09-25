from django import forms as django_forms
from django.contrib.auth import forms
from django.contrib.auth.forms import PasswordChangeForm

from utils.django_forms import add_attr

from .models import User


class UserChangeForm(forms.UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_attr(self.fields.get('email'), 'class', 'col-span-2')

    class Meta:
        model = User
        fields = ['picture', 'first_name', 'last_name', 'email']
        widgets = {
            'picture': django_forms.FileInput(
                attrs={
                    'class': 'col-span-2'
                }
            ),
            'first_name': django_forms.TextInput(
                attrs={
                    'placeholder': 'Digite seu nome'
                }
            ),
            'last_name': django_forms.TextInput(
                attrs={
                    'placeholder': 'Digite seu sobrenome'
                }
            ),
            'email': django_forms.TextInput(
                attrs={
                    'placeholder': 'Digite seu e-mail. Ex.: joao.silva@email.com'
                }
            )
        }
        labels = {
            'picture': 'Foto',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
        }


class UserChangePasswordForm(PasswordChangeForm):

    error_messages = {
        'password_incorrect': 'Sua senha atual está incorreto.',
        'password_mismatch': 'As senhas não conferem.'
    }

    old_password = django_forms.CharField(
        label='Senha Atual',
        strip=False,
        widget=django_forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True}
        ),
    )
    new_password1 = django_forms.CharField(
        label='Nova Senha',
        widget=django_forms.PasswordInput(
            attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    new_password2 = django_forms.CharField(
        label='Confirmar Nova Senha',
        strip=False,
        widget=django_forms.PasswordInput(
            attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User

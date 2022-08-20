from django import forms as django_forms
from django.contrib.auth import forms

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
            )
        }
        labels = {
            'picture': 'Foto',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
        }


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User

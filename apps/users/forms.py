from django.contrib.auth import forms

from .models import User


class UserChangeForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = [
            'picture',
            'first_name',
            'last_name',
            'email',
            'password',
        ]


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User

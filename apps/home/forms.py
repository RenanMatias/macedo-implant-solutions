from django import forms
from django.core.mail import send_mail

from utils.django_forms import add_placeholder


class ContactForm(forms.Form):
    """Form to send message to the company

    Args:
        forms (Django BaseForm): Create a form with name, e-mails and message fields
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['name'], 'Digite seu nome')
        add_placeholder(self.fields['email'], 'Digite seu e-mail')
        add_placeholder(self.fields['message'], 'Digite sua mensagem')

    name = forms.CharField(
        label='Nome',
        max_length=100,
        required=True
    )
    email = forms.EmailField(
        label='E-mail',
        required=True
    )
    message = forms.CharField(
        label='Mensagem',
        required=True,
        widget=forms.Textarea
    )

    def send_email(self, form):
        subject = "Contato do site"
        body = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message'],
        }
        message = f"Nome: {body['name']}\nE-mail: {body['email']}\nMensagem: {body['message']}"

        send_mail(
            subject,
            message,
            'admin@example.com',
            ['admin@example.com'],
        )

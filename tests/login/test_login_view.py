from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import resolve, reverse

from apps.login.views import LoginForm, LoginView


class LoginViewTest(TestCase):
    def test_login_view_function_is_correct(self):
        view = resolve(reverse('login'))
        self.assertIs(view.func.view_class, LoginView)

    def test_login_view_loads_status_code_200_ok(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_loads_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login/login.html')

    def test_login_view_loads_correct_login_form(self):
        response = self.client.get(reverse('login'))
        self.assertIsInstance(response.context['form'], LoginForm)

    def test_login_form_loads_correct_fields(self):
        response = self.client.get(reverse('login'))
        self.assertIn('username', response.context['form'].fields)
        self.assertIn('password', response.context['form'].fields)

    def test_login_form_add_placeholder_to_username_field(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(
            response.context['form'].fields['username'].widget.attrs['placeholder'],
            'Insira seu nome de usuário'
        )

    def test_login_form_add_placeholder_to_password_field(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(
            response.context['form'].fields['password'].widget.attrs['placeholder'],
            'Insira sua senha'
        )

    def test_login_form_loads_correct_type_for_password_field(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(
            response.context['form'].fields['password'].widget.input_type,
            'password'
        )

    def test_user_login_with_correct_credentials(self):
        User.objects.create_user(
            username='test_user',
            password='test_password'
        )
        response = self.client.post(
            reverse('login'),
            data={
                'username': 'test_user',
                'password': 'test_password'
            }
        )
        self.assertRedirects(response, reverse('core:dashboard'))

    def test_flash_message_loads_when_user_login_with_incorrect_credentials(self):
        User.objects.create_user(
            username='test_user',
            password='test_password'
        )
        response = self.client.post(
            reverse('login'),
            {
                'username': 'test_user',
                'password': 'test_password_incorrect'
            }
        )
        self.assertEqual(
            'Credenciais inválida.',
            list(get_messages(response.wsgi_request))[0].message
        )

    def test_flash_message_loads_when_fields_is_empty(self):
        response = self.client.post(
            reverse('login'),
            {
                'username': '',
                'password': ''
            }
        )
        self.assertEqual(
            'Nome de usuário ou senha inválida.',
            list(get_messages(response.wsgi_request))[0].message
        )

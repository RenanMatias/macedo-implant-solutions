from django.contrib.messages import get_messages
from django.core import mail
from django.test import TestCase
from django.urls import resolve, reverse

from apps.home.forms import ContactForm
from apps.home.views import HomeView


class HomeViewTest(TestCase):

    def test_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func.view_class, HomeView)

    def test_home_view_loads_status_code_200_OK(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/home.html')

    def test_home_view_loads_correct_form(self):
        response = self.client.get(reverse('home'))
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_flash_message_loads_when_user_form_is_submitted(self):
        response = self.client.post(
            reverse('home'),
            {
                'name': 'test_user',
                'email': 'test_user@test.com',
                'message': 'test_message',
            }
        )
        self.assertEqual(
            'Agradecemos seu contato, em breve entraremos em contato.',
            list(get_messages(response.wsgi_request))[0].message
        )

    def test_send_email_when_contact_form_is_submitted(self):
        self.client.post(
            reverse('home'),
            {
                'name': 'test_user',
                'email': 'test_user@test.com',
                'message': 'test_message',
            }
        )
        self.assertEqual(1, len(mail.outbox))

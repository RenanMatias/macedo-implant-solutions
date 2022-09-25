from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import resolve, reverse

from apps.login.views import LogoutView
from apps.users.models import User


class LogouViewTest(TestCase):
    def test_logout_view_function_is_correct(self):
        view = resolve(reverse('logout'))
        self.assertIs(view.func.view_class, LogoutView)

    def test_logout_view_loads_status_code_200_OK_when_user_logged_in(self):
        User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.client.login(
            username='testuser',
            password='12345'
        )
        response = self.client.get(reverse('logout'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout_view_loads_status_302_FOUND_when_user_not_logged_in(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_user_can_logout_successfully(self):
        User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.client.login(
            username='testuser',
            password='12345'
        )
        response = self.client.get(reverse('logout'), follow=True)
        self.assertEqual(
            'Logout realizado com sucesso.',
            list(get_messages(response.wsgi_request))[0].message
        )

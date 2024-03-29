from django.test import TestCase
from django.urls import resolve, reverse

from apps.core.views.client import ClientCreateView
from apps.users.models import User


def createUserAndLogin(self):
    User.objects.create_user(
        username='test_user',
        password='test_password'
    )
    self.client.login(
        username='test_user',
        password='test_password'
    )


class ClientCreateViewTest(TestCase):
    def test_client_create_view_function_is_correct(self):
        view = resolve(reverse('core:client_create'))
        self.assertIs(view.func.view_class, ClientCreateView)

    def test_client_create_view_loads_status_code_200_OK_when_user_logged_in(self):
        createUserAndLogin(self)
        response = self.client.get(reverse('core:client_create'))
        self.assertEqual(response.status_code, 200)

    def test_client_create_view_loads_status_302_FOUND_when_user_not_logged_in(self):
        response = self.client.get(reverse('core:client_create'))
        self.assertEqual(response.status_code, 302)

    def test_client_create_view_loads_correct_template(self):
        createUserAndLogin(self)
        response = self.client.get(reverse('core:client_create'))
        self.assertTemplateUsed(response, 'core/pages/client_create.html')

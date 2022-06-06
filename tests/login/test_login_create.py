from django.test import TestCase
from django.urls import resolve, reverse

from apps.login import views


class LoginCreateTest(TestCase):
    def test_login_create_function_is_correct(self):
        view = resolve(reverse('login:create'))
        self.assertIs(view.func.view_class, views.LoginCreate)

    def test_login_create_loads_status_code_200_ok(self):
        response = self.client.get(reverse('login:create'))
        self.assertEqual(response.status_code, 200)

    def test_login_create_loads_correct_template(self):
        response = self.client.get(reverse('login:create'))
        self.assertTemplateUsed(response, 'login/create.html')

from apps.login.views import site
from django.test import TestCase
from django.urls import resolve, reverse


class LoginViewTest(TestCase):
    def test_login_view_function_is_correct(self):
        view = resolve(reverse('login:login'))
        self.assertIs(view.func.view_class, site.LoginView)

    def test_login_view_loads_status_code_200_ok(self):
        response = self.client.get(reverse('login:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_loads_correct_template(self):
        response = self.client.get(reverse('login:login'))
        self.assertTemplateUsed(response, 'login/login.html')

# from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from apps.core.views import DashboardView


class DashboardViewTest(TestCase):

    def test_dashboard_view_function_is_correct(self):
        view = resolve(reverse('core:dashboard'))
        self.assertIs(view.func.view_class, DashboardView)

    def test_dashboard_view_loads_status_code_200_OK_when_user_logged_in(self):
        User.objects.create_user(
            username='test_user',
            password='test_password'
        )
        self.client.login(
            username='test_user',
            password='test_password'
        )
        response = self.client.get(reverse('core:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_loads_status_302_FOUND_when_user_not_logged_in(self):
        response = self.client.get(reverse('core:dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_view_loads_correct_template(self):
        User.objects.create_user(
            username='test_user',
            password='test_password'
        )
        self.client.login(
            username='test_user',
            password='test_password'
        )
        response = self.client.get(reverse('core:dashboard'))
        self.assertTemplateUsed(response, 'core/dashboard.html')

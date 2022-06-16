from django.test import TestCase
from django.urls import resolve, reverse

from apps.core.views import DashboardView


class DashboardViewTest(TestCase):

    def test_dashboard_view_function_is_correct(self):
        view = resolve(reverse('core:dashboard'))
        self.assertIs(view.func.view_class, DashboardView)

    def test_dashboard_view_loads_status_code_200_OK(self):
        response = self.client.get(reverse('core:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_loads_correct_template(self):
        response = self.client.get(reverse('core:dashboard'))
        self.assertTemplateUsed(response, 'core/dashboard.html')

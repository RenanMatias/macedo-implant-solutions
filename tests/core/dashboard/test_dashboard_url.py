from django.test import TestCase
from django.urls import reverse


class DashboardURLsTest(TestCase):
    def test_dashboard_url_is_correct(self):
        url = reverse('core:dashboard')
        self.assertEqual(url, '/dashboard/')

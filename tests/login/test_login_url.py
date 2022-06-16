from unittest import TestCase
from django.urls import reverse


class LoginURLsTest(TestCase):
    def test_login_view_url_is_correct(self):
        url = reverse('login')
        self.assertEqual(url, '/login/')

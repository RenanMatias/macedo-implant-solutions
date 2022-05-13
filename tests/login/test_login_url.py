from django.test import TestCase
from django.urls import reverse


class LoginURLsTest(TestCase):
    def test_login_url_is_correct(self):
        url = reverse('login:login')
        self.assertEqual(url, '/login/')

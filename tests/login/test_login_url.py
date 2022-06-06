from django.test import TestCase
from django.urls import reverse


class LoginURLsTest(TestCase):
    def test_login_view_url_is_correct(self):
        url = reverse('login:login')
        self.assertEqual(url, '/login/')

    def test_create_url_is_correct(self):
        url = reverse('login:create')
        self.assertEqual(url, '/login/create/')

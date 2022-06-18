from unittest import TestCase

from django.urls import reverse


class LogoutURLsTest(TestCase):
    def test_logout_view_url_is_correct(self):
        url = reverse('logout')
        self.assertEqual(url, '/logout/')

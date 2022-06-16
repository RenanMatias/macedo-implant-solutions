from unittest import TestCase

from django.urls import reverse


class HomeURLsTest(TestCase):

    def test_home_url_is_correct(self):
        url = reverse('home')
        self.assertEqual(url, '/')

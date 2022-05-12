from django.test import TestCase
from django.urls import reverse


class HomeURLsTest(TestCase):

    def test_home_url_is_correct(self):
        url = reverse('home:home')
        self.assertEqual(url, '/')

from unittest import TestCase

from django.urls import reverse


class ClientURLsTest(TestCase):
    def test_client_list_url_is_correct(self):
        url = reverse('core:client_list')
        self.assertEqual(url, '/clientes/')

    def test_client_create_url_is_correct(self):
        url = reverse('core:client_create')
        self.assertEqual(url, '/clientes/create/')

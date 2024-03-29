from unittest import TestCase

from django.urls import reverse


class ClientURLsTest(TestCase):
    def test_client_list_url_is_correct(self):
        url = reverse('core:client_list')
        self.assertEqual(url, '/clients/')

    def test_client_create_url_is_correct(self):
        url = reverse('core:client_create')
        self.assertEqual(url, '/clients/create/')

    def test_client_search_url_is_correct(self):
        url = reverse('core:client_search')
        self.assertEqual(url, '/clients/search/')

    def test_client_export_excel_url_is_correct(self):
        url = reverse('core:client_export_excel')
        self.assertEqual(url, '/clients/export_excel/')

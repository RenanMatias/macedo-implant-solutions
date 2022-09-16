from unittest import TestCase

from utils.factory import make_client


class FactoryTest(TestCase):
    def test_make_client_is_working(self):

        client = make_client()

        self.assertIn('nome', client)
        self.assertIn('tipo', client)
        self.assertIn('status', client)

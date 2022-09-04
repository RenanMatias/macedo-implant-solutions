from unittest import TestCase

from django.core.exceptions import ValidationError

from utils.django_forms import strong_password


class DjangoFormTest(TestCase):
    def test_strong_password_raise_error(self):
        password = '123456'
        with self.assertRaises(ValidationError):
            strong_password(password)

    def test_strong_password_not_raise_error(self):
        password = '@Bc123456'
        self.assertTrue(strong_password(password))

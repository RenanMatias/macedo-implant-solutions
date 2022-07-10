from django.test import TestCase

from apps.users.models import User


class UserModelTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='username',
            password='password'
        )
        self.client.force_login(self.user)
        return super().setUp()

    def test_first_letter_user_first_name_without_first_name(self):
        self.assertEqual(self.user.first_letter_first_name(), None)

    def test_first_letter_user_first_name_with_first_name(self):
        self.user.first_name = 'John'
        self.user.full_clean()
        self.user.save()
        self.assertEqual(self.user.first_letter_first_name(), 'J')

    def test_first_letter_user_last_name_without_last_name(self):
        self.assertEqual(self.user.first_letter_last_name(), None)

    def test_first_letter_user_first_name_with_last_name(self):
        self.user.last_name = 'Doe'
        self.user.full_clean()
        self.user.save()
        self.assertEqual(self.user.first_letter_last_name(), 'D')

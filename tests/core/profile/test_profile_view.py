from django.test import TestCase
from django.urls import resolve, reverse

from apps.core.views.profile import ProfileView
from apps.users.models import User


def create_user():
    user = User.objects.create_user(
        username='test_user',
        password='test_password'
    )
    return user


def login_user(self):
    self.client.login(
        username='test_user',
        password='test_password'
    )


class ProfileViewTest(TestCase):

    def test_profile_view_function_is_correct(self):
        view = resolve(reverse('core:profile'))
        self.assertIs(view.func.view_class, ProfileView)

    def test_profile_view_loads_status_302_FOUND_when_user_not_logged_in(self):
        create_user()
        response = self.client.get(reverse('core:profile'))
        self.assertEqual(response.status_code, 302)

    def test_profile_view_loads_status_code_200_OK_when_user_logged_in(self):
        create_user()
        login_user(self)
        response = self.client.get(reverse('core:profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_loads_correct_template(self):
        create_user()
        login_user(self)
        response = self.client.get(reverse('core:profile'))
        self.assertTemplateUsed(response, 'core/profile.html')

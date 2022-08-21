from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import resolve, reverse

from apps.core.views.profile import ProfileChangePasswordView, ProfileView
from apps.users.forms import UserChangeForm
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
        view = resolve(reverse('core:profile', kwargs={'pk': 1}))
        self.assertIs(view.func.view_class, ProfileView)

    def test_profile_view_loads_status_302_FOUND_when_user_not_logged_in(self):
        create_user()
        response = self.client.get(reverse('core:profile', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_profile_view_loads_status_code_200_OK_when_user_logged_in(self):
        create_user()
        login_user(self)
        response = self.client.get(reverse('core:profile', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_loads_correct_template(self):
        create_user()
        login_user(self)
        response = self.client.get(reverse('core:profile', kwargs={'pk': 1}))
        self.assertTemplateUsed(response, 'core/profile.html')


class UserChangeProfileIntegrationTest(TestCase):

    def setUp(self, *args, **kwargs):
        self.form_data = {
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@anyemail.com'
        }
        return super().setUp(*args, **kwargs)

    def test_fields_cannot_be_empty(self):
        form = UserChangeForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_save_method(self):
        form = UserChangeForm(data=self.form_data)
        form.save()
        self.assertEqual(User.objects.count(), 1)

    def test_flash_message_loads_when_user_form_is_submitted(self):
        create_user()
        login_user(self)

        response = self.client.post(
            reverse('core:profile', kwargs={'pk': 1}),
            {
                'first_name': 'first',
                'last_name': 'last',
                'email': 'email@anyemail.com',
            }
        )
        self.assertEqual(
            'Dados atualizados com sucesso.',
            list(get_messages(response.wsgi_request))[0].message
        )


class ProfileChangePasswordViewTest(TestCase):

    def test_profile_change_password_view_function_is_correct(self):
        view = resolve(reverse('core:profile_change_pass', kwargs={'pk': 1}))
        self.assertIs(view.func.view_class, ProfileChangePasswordView)

    def test_profile_change_password_view_loads_status_302_FOUND_when_user_not_logged_in(self):
        create_user()
        response = self.client.get(
            reverse('core:profile_change_pass', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_profile_change_password_view_loads_status_code_200_OK_when_user_logged_in(self):
        create_user()
        login_user(self)
        response = self.client.get(
            reverse('core:profile_change_pass', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_profile_change_password_view_loads_correct_template(self):
        create_user()
        login_user(self)
        response = self.client.get(
            reverse('core:profile_change_pass', kwargs={'pk': 1}))
        self.assertTemplateUsed(response, 'core/profile_change_pass.html')


class UserChangePasswordIntegrationTest(TestCase):

    def setUp(self, *args, **kwargs):
        self.form_data = {
            'old_password': 'test_password',
            'new_password1': 'new_password',
            'new_password2': 'new_password'
        }
        return super().setUp(*args, **kwargs)

    def test_fields_cannot_be_empty(self):
        form = UserChangeForm(data=self.form_data)
        self.assertTrue(form.is_valid())

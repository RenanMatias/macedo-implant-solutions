from django.urls import resolve, reverse

from apps.core.views.client import ClientListViewBase
from tests.core.client.test_client_base import ClientTestBase


class ClientListViewTest(ClientTestBase):

    def test_client_list_view_function_is_correct(self):
        view = resolve(reverse('core:client_list'))
        self.assertIs(view.func.view_class, ClientListViewBase)

    def test_client_list_view_loads_status_code_200_OK_when_user_logged_in(self):
        self.make_user()
        response = self.client.get(reverse('core:client_list'))
        self.assertEqual(response.status_code, 200)

    def test_client_list_view_loads_status_302_FOUND_when_user_not_logged_in(self):
        response = self.client.get(reverse('core:client_list'))
        self.assertEqual(response.status_code, 302)

    def test_client_list_view_loads_correct_template(self):
        self.make_user()
        response = self.client.get(reverse('core:client_list'))
        self.assertTemplateUsed(response, 'core/pages/client_list.html')

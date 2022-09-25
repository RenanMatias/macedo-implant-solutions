from django.urls import resolve, reverse

from apps.core.views.client import ClientListViewSearch
from tests.core.client.test_client_base import ClientTestBase


class ClientListViewSearchTest(ClientTestBase):

    def test_client_search_view_is_correct(self):
        url = reverse('core:client_search')
        view = resolve(url)
        self.assertIs(view.func.view_class, ClientListViewSearch)

    def test_client_search_view_loads_correct_template(self):
        self.make_user()
        url = reverse('core:client_search') + '?q=teste'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'core/pages/client_list.html')

    def test_client_search_raises_404_if_no_search_term(self):
        self.make_user()
        url = reverse('core:client_search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def teste_client_search_term_is_on_page_title_and_escaped(self):
        self.make_user()
        url = reverse('core:client_search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Cliente pesquisa por &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )

    def test_client_search_can_find_client_by_title(self):
        user = self.make_user()

        nome1 = 'This is client one'
        nome2 = 'This is client two'

        client1 = self.make_client(nome=nome1, username_data=user)
        client2 = self.make_client(nome=nome2, username_data=user)

        url = reverse('core:client_search')
        response1 = self.client.get(url + f'?q={nome1}')
        response2 = self.client.get(url + f'?q={nome2}')
        response_both = self.client.get(url + '?q=this')

        self.assertIn(client1, response1.context['clients'])
        self.assertNotIn(client2, response1.context['clients'])

        self.assertIn(client2, response2.context['clients'])
        self.assertNotIn(client1, response2.context['clients'])

        self.assertIn(client1, response_both.context['clients'])
        self.assertIn(client2, response_both.context['clients'])

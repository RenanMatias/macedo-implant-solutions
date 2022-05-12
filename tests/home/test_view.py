from apps.home.views import home_view
from django.test import TestCase
from django.urls import resolve, reverse


class HomeViewTest(TestCase):

    def test_home_view_function_is_correct(self):
        view = resolve(reverse('home:home'))
        self.assertIs(view.func, home_view)

    def test_home_view_loads_status_code_200_OK(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_loads_correct_template(self):
        response = self.client.get(reverse('home:home'))
        self.assertTemplateUsed(response, 'home/home.html')

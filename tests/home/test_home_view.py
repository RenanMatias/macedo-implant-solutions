from django.test import TestCase
from django.urls import resolve, reverse

from apps.home.forms import HomeForm
from apps.home.views import HomeView


class HomeViewTest(TestCase):

    def test_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func.view_class, HomeView)

    def test_home_view_loads_status_code_200_OK(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/home.html')

    def test_home_view_loads_correct_form(self):
        response = self.client.get(reverse('home'))
        self.assertIsInstance(response.context['form'], HomeForm)

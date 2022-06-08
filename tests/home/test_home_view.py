from django.test import TestCase
from django.urls import resolve, reverse

from apps.home.views import site


class HomeViewTest(TestCase):

    def test_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func.view_class, site.HomeView)

    def test_home_view_loads_status_code_200_OK(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/home.html')

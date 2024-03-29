from unittest import TestCase

from django.urls import reverse


class ProfileURLsTest(TestCase):
    def test_profile_url_is_correct(self):
        url = reverse('core:profile', kwargs={'pk': 1})
        self.assertEqual(url, '/profile/1/')

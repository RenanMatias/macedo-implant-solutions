import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from PIL import Image

from apps.users.models import User

img_name = 'test_image.jpg'
img_path = settings.MEDIA_ROOT / img_name


def create_image(width, height):
    """Create a PIL image of the given size."""
    image = Image.new('RGB', (width, height))
    image.save(img_path)
    return image


class UserModelTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='username',
            password='password'
        )

        self.client.force_login(self.user)
        return super().setUp()

    def tearDown(self) -> None:
        if self.user.picture:
            if os.path.exists(self.user.picture.path):
                os.remove(self.user.picture.path)

        if os.path.exists(img_path):
            os.remove(img_path)

        return super().tearDown()

    def test_first_letter_user_first_name_without_first_name(self):
        self.assertEqual(self.user.first_letter_first_name(), None)

    def test_first_letter_user_first_name_with_first_name(self):
        self.user.first_name = 'John'
        self.user.last_name = 'Doe'
        self.user.email = 'john.doe@email.com'
        self.user.full_clean()
        self.user.save()
        self.assertEqual(self.user.first_letter_first_name(), 'J')

    def test_first_letter_user_last_name_without_last_name(self):
        self.assertEqual(self.user.first_letter_last_name(), None)

    def test_first_letter_user_first_name_with_last_name(self):
        self.user.first_name = 'John'
        self.user.last_name = 'Doe'
        self.user.email = 'john.doe@email.com'
        self.user.full_clean()
        self.user.save()
        self.assertEqual(self.user.first_letter_last_name(), 'D')

    def test_user_upload_picture_with_size_lower_than_max_size(self):
        image = create_image(100, 100)

        self.user.picture = SimpleUploadedFile(
            img_name,
            open(img_path, 'rb').read()
        )
        original_width, _ = image.size
        self.user.save()
        self.assertLess(original_width, 460)

    def test_user_upload_picture_with_size_greater_than_max_size(self):
        image = create_image(500, 500)

        self.user.picture = SimpleUploadedFile(
            img_name,
            open(img_path, 'rb').read()
        )
        original_width, _ = image.size
        self.user.save()
        self.assertGreater(original_width, 460)

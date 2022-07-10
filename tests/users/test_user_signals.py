import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from apps.users.models import User


class UserSignalsTest(TestCase):

    def setUp(self) -> None:
        self.user_without_picture = User.objects.create_user(
            username='test_user_without_picture',
            password='test_password'
        )

        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        # user_picture = tempfile.NamedTemporaryFile(suffix='.jpg').name
        self.user_with_picture = User.objects.create_user(
            username='test_user_with_picture',
            password='test_password',
            picture=SimpleUploadedFile(
                'small.gif',
                small_gif,
                content_type='image/gif'
            )
        )
        return super().setUp()

    def tearDown(self) -> None:
        if os.path.exists(self.user_with_picture.picture.path):
            os.remove(self.user_with_picture.picture.path)
        return super().tearDown()

    def test_create_new_user_without_image_file(self):
        self.assertEqual(self.user_without_picture.picture, '')

    def test_create_new_user_with_image_file(self):
        self.assertNotEqual(self.user_with_picture.picture, '')

    def test_delete_user_without_image_file_raise_FileNotFoundError(self):
        self.user_with_picture.delete()
        with self.assertRaises(FileNotFoundError):
            os.remove(self.user_with_picture.picture.path)

    def test_user_update_with_same_image_file(self):
        user_with_picture = self.user_with_picture
        picture = user_with_picture.picture
        user_with_picture.first_name = 'test_first_name'
        user_with_picture.save()
        self.assertIn(picture.path, user_with_picture.picture.path)

    def test_user_change_image_file_and_old_image_file_is_deleted(self):
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )

        user_with_picture = self.user_with_picture
        picture = user_with_picture.picture
        user_with_picture.picture = SimpleUploadedFile(
            'small.gif',
            small_gif,
            content_type='image/gif'
        )
        user_with_picture.save()
        self.assertNotIn(picture.path, user_with_picture.picture.path)

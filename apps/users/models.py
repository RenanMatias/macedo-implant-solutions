import os
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


def path_and_rename(instance, filename):
    upload_to = 'users/pictures'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class User(AbstractUser):
    picture = models.ImageField(
        upload_to=path_and_rename,
        blank=True,
        default=''
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()

    def first_letter_first_name(self):
        if self.first_name == '':
            return
        first_name = self.first_name
        first_letter = first_name[0]
        return first_letter

    def first_letter_last_name(self):
        if self.last_name == '':
            return
        last_name = self.last_name
        first_letter = last_name[0]
        return first_letter

    @staticmethod
    def resize_image(image, new_width=460):
        """Resize user image file to 460 width if original width is grater than

        Args:
            image (image): Original image
            new_width (int, optional): size to be resized. Defaults to 460.
        """
        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        image_pillow = Image.open(image_full_path)
        original_width, original_height = image_pillow.size

        if original_width <= new_width:
            image_pillow.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_image = image_pillow.resize(
            (
                new_width,
                new_height
            ),
            Image.Resampling.LANCZOS
        )

        new_image.save(
            image_full_path,
            optimize=True,
            quality=60,
        )

    def save(self, *args, **kwargs):
        saved = super().save(*args, **kwargs)

        if self.picture:
            self.resize_image(self.picture)

        return saved

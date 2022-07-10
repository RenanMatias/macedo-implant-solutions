import os
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


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

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    picture = models.ImageField(
        upload_to='users/pictures/%Y/%m/%d',
        blank=True,
        default=''
    )

    def first_letter_first_name(self):
        return self.first_name[0]

    def first_letter_last_name(self):
        return self.last_name[0]

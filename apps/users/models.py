from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    picture = models.ImageField(
        upload_to='users/pictures/%Y/%m/%d',
        blank=True,
        default=''
    )

import os

from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from apps.users.models import User


def delete_picture(instance):
    os.remove(instance.picture.path)


@receiver(pre_delete, sender=User)
def user_delete(sender, instance, *args, **kwargs):
    """Delete image file when user is deleted

    Args:
        sender (Model): User
        instance (User): user logged
    """
    old_instance = User.objects.filter(pk=instance.pk).first()

    delete_picture(old_instance)


@receiver(pre_save, sender=User)
def user_picture_update(sender, instance, *args, **kwargs):
    """Delete old image file when user uploads new image file

    Args:
        sender (Model): User
        instance (User): user logged
    """
    old_instance = User.objects.filter(pk=instance.pk).first()

    if not old_instance:
        return

    is_new_picture = old_instance.picture != instance.picture

    if is_new_picture:
        delete_picture(old_instance)

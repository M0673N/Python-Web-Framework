from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import os

from petstagram.accounts.models import ProfileAdditionalData

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = ProfileAdditionalData(
            user=instance,
        )

        profile.save()


@receiver(pre_save, sender=ProfileAdditionalData)
def delete_old_file(sender, instance, **kwargs):
    # big thanks to stack overflow
    # on creation, signal callback won't be triggered
    # if instance._state.adding and not istance.pk:
    #     return False

    try:
        old_file = sender.objects.get(pk=instance.pk).profile_image
    except sender.DoesNotExist:
        return False

    # comparing the new file with the old one
    file = instance.profile_image
    if not old_file == file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

from django.db import models

from pythons_auth.models import PythonsUser


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
    )
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    is_complete = models.BooleanField(
        default=False,
    )
    user = models.OneToOneField(
        PythonsUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

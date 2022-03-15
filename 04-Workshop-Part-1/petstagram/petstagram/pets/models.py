from django.core.exceptions import ValidationError
from django.db import models


def positive_number_validator(value):
    if value < 0:
        raise ValidationError('Make sure the age is a positive number!')


class Pet(models.Model):
    CAT_CHOICE = 'cat'
    DOG_CHOICE = 'dog'
    PARROT_CHOICE = 'parrot'
    type = models.CharField(choices=[(CAT_CHOICE, 'Cat'), (DOG_CHOICE, 'Dog'), (PARROT_CHOICE, 'Parrot')], max_length=6)
    name = models.CharField(max_length=6)
    age = models.IntegerField(validators=[positive_number_validator])
    description = models.TextField()
    image_url = models.ImageField()


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

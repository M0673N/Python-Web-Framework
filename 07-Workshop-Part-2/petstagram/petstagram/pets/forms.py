import os

from django import forms
from django.conf import settings

from petstagram.pets.models import Pet


class CreatePetForm(forms.ModelForm):
    type = forms.ChoiceField(choices=[("dog", "dog"), ("cat", "cat"), ("parrot", "parrot")], required=True,
                             widget=forms.Select(
                                 attrs={
                                     'class': 'form-control'
                                 },

                             ))
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    age = forms.IntegerField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number'
        }
    ))
    image_url = forms.FileField(required=True, widget=forms.FileInput(
        attrs={
            'class': 'form-control'
        }
    ))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control rounded-2'
    }))

    class Meta:
        model = Pet
        fields = ('type', 'name', 'age', 'description', 'image_url')


class EditPetForm(CreatePetForm):
    def save(self, commit=True):
        db_pet = Pet.objects.get(pk=self.instance.id)
        if commit:
            image_path = os.path.join(settings.MEDIA_ROOT, str(db_pet.image))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }

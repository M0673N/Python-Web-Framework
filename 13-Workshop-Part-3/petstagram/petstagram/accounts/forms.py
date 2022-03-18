from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from petstagram.mixins import BootstrapFormMixin
from petstagram.accounts.models import ProfileAdditionalData

UserModel = get_user_model()


class LoginForm(AuthenticationForm, BootstrapFormMixin):
    pass


class RegisterForm(UserCreationForm, BootstrapFormMixin):
    class Meta:
        model = UserModel
        fields = ('email',)


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = ProfileAdditionalData
        fields = ('profile_image',)

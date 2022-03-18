from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from pythons_auth.forms import LoginForm, RegisterForm
from pythons_auth.models import PythonsUser


def logout_view(request):
    logout(request)
    return redirect('index')


class RegisterView(CreateView):
    template_name = 'signup.html'
    model = PythonsUser
    form_class = RegisterForm
    success_url = reverse_lazy('index')


class PythonsLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('index')

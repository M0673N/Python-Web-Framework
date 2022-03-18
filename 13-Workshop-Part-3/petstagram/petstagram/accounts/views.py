from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from petstagram.accounts.forms import LoginForm, RegisterForm, ProfileForm
from petstagram.accounts.models import ProfileAdditionalData
from petstagram.pets.models import Pet


class LoginUserView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    next_page = reverse_lazy('landing')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('landing')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


def logout_user(request):
    logout(request)
    return redirect('landing')


class ProfileDetailsView(LoginRequiredMixin, FormView):
    template_name = 'user_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = ProfileAdditionalData.objects.get(pk=request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = ProfileAdditionalData.objects.get(pk=request.user.id)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.profile_image = form.cleaned_data['profile_image']
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pets'] = Pet.objects.filter(user_id=self.request.user.id)
        context['profile'] = self.object

        return context

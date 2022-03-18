from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from petstagram.accounts.forms import LoginForm, RegisterForm, ProfileForm
from petstagram.accounts.models import ProfileAdditionalData
from petstagram.pets.models import Pet


def logout_view(request):
    logout(request)
    return redirect('landing')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('landing')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pet list')

    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)


def profile_detail_view(request):
    profile = ProfileAdditionalData.objects.get(user_id=request.user.id)
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    else:
        form = ProfileForm()

    context = {
        'form': form,
        'pets': Pet.objects.filter(user_id=request.user.id),
        'profile': profile
    }

    return render(request, 'user_profile.html', context)

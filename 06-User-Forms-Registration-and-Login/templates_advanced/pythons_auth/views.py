from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from pythons_auth.forms import LoginForm, RegisterForm


def logout_view(request):
    logout(request)
    return redirect('index')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
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
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)

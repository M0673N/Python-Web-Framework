from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .decorators import check_user_able_to_see_page
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


# @allowed_groups(['User'])
@check_user_able_to_see_page('User')
def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        data = req.POST
        form = PythonCreateForm(data, req.FILES)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')


def login_view(request):
    user = authenticate(username='test_user', password='22222222a')
    if user:
        login(request, user)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')

from django.shortcuts import render, redirect

from .decorators import check_user_able_to_see_page
from .forms import PythonCreateForm
from .models import Python


def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


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

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import PythonCreateForm
from .mixins import AnyGroupRequiredMixin
from .models import Python


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'
    paginate_by = 5


class PythonCreateView(CreateView, AnyGroupRequiredMixin):
    required_groups = ['User']
    template_name = 'create.html'
    model = Python
    form_class = PythonCreateForm
    # fields = '__all__'
    success_url = reverse_lazy('index')

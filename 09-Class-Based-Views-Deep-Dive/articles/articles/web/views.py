from django.urls import reverse_lazy, reverse
from django.views import generic as views

from articles.web.models import Article, Source


class ArticleCreateView(views.CreateView):
    model = Article
    template_name = 'create-article.html'
    success_url = reverse_lazy('home')
    fields = '__all__'


class SourceCreateView(views.CreateView):
    model = Source
    template_name = 'create-source.html'
    # success_url = reverse_lazy('index')
    fields = '__all__'

    def get_success_url(self):
        return reverse('details source', kwargs={
            'pk': self.object.id,
        })


class HomeView(views.ListView):
    model = Article
    template_name = 'home.html'


class SourceDetailsView(views.ListView):
    model = Source
    template_name = 'source-details.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['source'] = Source.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Source.objects.get(pk=self.kwargs['pk']).article_set.all()


class SourcesListView(views.ListView):
    model = Source
    template_name = 'sources.html'

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.views import generic

from apps.news.models import News
from apps.news.forms import NewsCreateForm, NewsUpdateForm

class NewsListView(generic.ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'


class NewsCreateView(LoginRequiredMixin, generic.CreateView):
    model = News
    form_class = NewsCreateForm
    template_name = 'news/create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'news'


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = News
    form_class = NewsUpdateForm
    template_name = 'news/update.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        news = self.get_object()
        return self.request.user == news.author or self.request.user.is_superuser


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = News
    template_name = 'news/delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        news = self.get_object()
        return self.request.user == news.author or self.request.user.is_superuser

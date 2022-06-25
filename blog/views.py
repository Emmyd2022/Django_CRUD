from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.urls import reverse, reverse_lazy
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')


class PostDeleteView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog: all')

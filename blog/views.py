from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
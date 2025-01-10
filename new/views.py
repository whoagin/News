from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    ordering = ['-publication_date']
    template_name = 'news.html'
    context_object_name = 'news'


class PostDetailView(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


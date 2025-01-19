from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post
from .filters import PostFilter


# Create your views here.

class PostListView(ListView):
    model = Post
    ordering = ['-publication_date']
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostSearchListView(ListView):
    model = Post
    ordering = ['-publication_date']
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        # context['post_form'] = PostForm(self.get_queryset())
        context['post_form'] = PostForm
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'edit_new.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = 'NE'
        post.author_id = 4
        return super().form_valid(form)


class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'edit_new.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = 'AR'
        post.author_id = 4
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'edit_new.html'


class ArticleUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'edit_new.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'delete_new.html'
    success_url = reverse_lazy('news_list')


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'delete_new.html'
    success_url = reverse_lazy('news_list')

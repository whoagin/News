from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
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


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('new.add_post', )
    form_class = PostForm
    model = Post
    template_name = 'edit_new.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = 'NE'
        post.author_id = 4
        return super().form_valid(form)


class ArticleCreate(PermissionRequiredMixin,CreateView):
    permission_required = ('new.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'edit_new.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = 'AR'
        post.author_id = 4
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('new.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'edit_new.html'


class ArticleUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = ('new.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'edit_new.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('new.delete_post',)
    model = Post
    template_name = 'delete_new.html'
    success_url = reverse_lazy('news_list')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('new.delete_post',)
    model = Post
    template_name = 'delete_new.html'
    success_url = reverse_lazy('news_list')

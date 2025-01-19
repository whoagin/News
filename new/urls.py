from django.urls import path
from .views import PostListView, PostDetailView, PostSearchListView, PostCreate, PostUpdate, PostDelete, ArticleCreate, \
    ArticleUpdate, ArticleDelete

urlpatterns = [
    path('', PostListView.as_view(), name='news_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('search/', PostSearchListView.as_view(), name='post_search'),
    path('news/create', PostCreate.as_view(), name='post_create'),
    path('article/create', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='post_delete'),

]

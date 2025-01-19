import django_filters
from django.forms import DateInput
from django_filters import FilterSet, CharFilter
from .models import Post


class PostFilter(FilterSet):
    title = django_filters.CharFilter(field_name='title',lookup_expr='icontains',label='Заголовок')
    author = django_filters.CharFilter(field_name='author_id__user_id__username',lookup_expr='icontains', label='Автор')
    publication_date = django_filters.DateTimeFilter(field_name='publication_date', lookup_expr='gte',label='Дата',widget=DateInput(attrs={'type': 'date'},format='%d.%m.%Y'))

    class Meta:
        model = Post

        fields = {
            # 'title': ['icontains'],
            # 'author_id__user_id__username': ['icontains'],
            # 'publication_date': ['gte'],
            'title','author','publication_date'
        }

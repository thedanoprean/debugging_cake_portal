import django_filters

from .models import *
from django_filters import DateFilter


class PostFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')

    class Meta:
        model = Post
        fields = ('title', 'author', 'post_tag',)

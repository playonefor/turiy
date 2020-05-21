from django_filters import rest_framework as filters
from django.db.models import Q
from users.models import tGroup


class tGroupFilter(filters.FilterSet):
    '''
    用户过滤
    '''

    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = tGroup
        fields = ('name',)

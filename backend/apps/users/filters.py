from django_filters import rest_framework as filters
from django.db.models import Q

from django.contrib.auth import get_user_model
from users.models import tGroup

User = get_user_model()


class UsersFilter(filters.FilterSet):
    '''
    用户过滤
    '''

    username = filters.CharFilter(lookup_expr='icontains')
    mobile = filters.CharFilter(lookup_expr='icontains')
    email = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ('username', 'mobile', 'email', 'is_active')


class tGroupFilter(filters.FilterSet):
    '''
    用户组过滤
    '''

    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = tGroup
        fields = ('name',)

from django_filters import rest_framework as filters
from django.db.models import Q

from perm.models import PerMisson


class PerMissonFilter(filters.FilterSet):

    """权限过滤"""

    class Meta:
        model = PerMisson
        fields = ('id', 'name')

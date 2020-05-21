from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from perm.models import PerMisson
from perm.serializers import PermListSerializer, \
    PermDetailSerializer, \
    PermCreateSerializer


# 权限分页
class PermissonPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


# 权限视图
class PermissonViewSet(viewsets.ModelViewSet):
    queryset = PerMisson.objects.all()
    serializer_class = PermDetailSerializer
    pagination_class = PermissonPagination
    # filter_backends =
    # filter_class =

    def get_serializer_class(self):
        if self.action == 'list':
            return PermListSerializer
        if self.action == 'create':
            return PermCreateSerializer
        return PermDetailSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from perm.models import PerMisson
from perm.filters import PerMissonFilter
from application.models import Application
from users.models import tGroup
from django.contrib.auth import get_user_model
from perm.serializers import PermListSerializer, \
    PermDetailSerializer, \
    PermCreateSerializer, \
    PermListSimpleSerializer, \
    PermUserSerializer, \
    PermAppSerializer, \
    PermtGroupSerializer

User = get_user_model()


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
    filter_backends = (DjangoFilterBackend,)
    filter_class = PerMissonFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return PermListSerializer
        if self.action == 'create':
            return PermCreateSerializer
        return PermDetailSerializer

    @action(detail=False, methods=['get'], name="get all permisson", url_path="getall")
    def get_perm_all(self, request, pk=None):
        permsqs = PerMisson.objects.all()
        serializer = PermListSimpleSerializer(permsqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], name="get all users", url_path="getusers")
    def get_all_users(self, request, pk=None):
        users = User.objects.all()
        serializer = PermUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], name="get all apps", url_path="getapps")
    def get_all_apps(self, request, pk=None):
        apps = Application.objects.all()
        serializer = PermAppSerializer(apps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], name="get all groups", url_path="getgroups")
    def get_all_tgroups(self, request, pk=None):
        tgroups = tGroup.objects.all()
        serializer = PermtGroupSerializer(tgroups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

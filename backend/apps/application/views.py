from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from application.models import Application
from application.serializers import ApplicationDetailSerializer, \
    ApplicationCreateSerializer,\
    ApplicationListSerializer




# 应用分页
class ApplicationPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


# 应用视图
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationDetailSerializer
    pagination_class = ApplicationPagination
    # filter_backends =
    # filter_class =

    def get_serializer_class(self):
        if self.action == 'list':
            return ApplicationListSerializer
        if self.action == 'create':
            return ApplicationCreateSerializer
        return ApplicationDetailSerializer

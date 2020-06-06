from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
# from rest_framework import filters
from .filters import UsersFilter, tGroupFilter
from rest_framework import viewsets
# from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from users.models import tGroup
from users.serializers import UserSerializer, UserCreateSerializer, UserSimpleSerializer, \
    tGroupListSerializer, tGroupDetailSerializer, tGroupCreateSerializer, tGroupPermAppDetailSerializer, \
    tGroupUpdateSerializer


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


User = get_user_model()

'''
重写以Token返回自定义响应.
def jwt_response_payload_handler(token, user=None, request=None):
    return {
                'id': UserSerializer(user, context={'request':request}).data['id'],
                'username': UserSerializer(user, context={'request':request}).data['username'],
                'token': token
            }
'''


# 重写以Token返回自定义响应.
class CustomObtainJSONWebToken(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainJSONWebToken, self).post(request,
                                                              *args,
                                                              **kwargs
                                                              )
        # get token
        token = response.data.get('token', '')

        # custom response
        if token:
            user = jwt_decode_handler(token)
            userobj = User.objects.get(pk=user.get('user_id'))
        else:
            req = request.data
            password = req.get('password', '')
            username = req.get('username', '')
            if not username and not password:
                return Response(
                    {
                        'msg': '用户名和密码不能为空',
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            try:
                userobj = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response(
                    {
                        'msg': '用户不存在',
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            if not userobj.check_password(password):
                return Response(
                    {
                        'msg': '密码错误'
                    },
                    status.HTTP_401_UNAUTHORIZED
                )

        payload = jwt_payload_handler(userobj)
        token = jwt_encode_handler(payload)
        userser = UserSerializer(userobj).data
        return Response(
            {
                'id': userser.get('id'),
                'username': userser.get('username'),
                'token': token
            }
        )


# 用户列表分页
class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


# 用户组列表分页
class tGroupPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


# 用户视图
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = UsersFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer


# 用户组视图
class tGroupViewSet(viewsets.ModelViewSet):
    queryset = tGroup.objects.all()
    pagination_class = tGroupPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = tGroupFilter
    serializer_class = tGroupDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return tGroupListSerializer
        if self.action == 'create':
            return tGroupCreateSerializer
        if self.action == 'update':
            return tGroupUpdateSerializer
        return tGroupDetailSerializer

    @action(detail=True, methods=['put'], name='delete user from usergroup')
    def delete_user_group(self, request, pk=None):
        try:
            group = tGroup.objects.get(pk=pk)
        except tGroup.DoesNotExist:
            raise Http404
        try:
            user = User.objects.get(pk=request.data.get('id'))
        except User.DoesNotExist:
            raise Http404

        group.users.remove(user)

        return Response({'msg': 'delete success'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'], name='group outside user')
    def group_outside_user(self, request, pk=None):
        users = User.objects.exclude(tgroup__id=pk)
        serializer = UserSimpleSerializer(users, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'], name="add user to group")
    def add_userto_group(self, request, pk=None):
        try:
            group = tGroup.objects.get(pk=pk)
        except tGroup.DoesNotExist:
            raise Http404

        if "users" not in request.data:
            return Response({
                'msg': 'params user not define'
            })

        users = []
        for userid in request.data.get('users'):
            try:
                user = User.objects.get(pk=userid)
            except User.DoesNotExist:
                raise Http404

            if user in group.users.all():
                continue

            group.users.add(user)
            users.append(user)

        serializer = UserSimpleSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], name="get group permisson apps")
    def get_group_permapp(self, request, pk=None):
        try:
            group = tGroup.objects.get(pk=pk)
        except tGroup.DoesNotExist:
            raise Http404

        serializer = tGroupPermAppDetailSerializer(group)

        return Response(serializer.data, status=status.HTTP_200_OK)


'''
用户组剔除成员
class tGroupDeleteUserApiView(APIView):
    def post(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        return Response({'msg': '删除成功'}, status=status.HTTP_200_OK)

    def get(self, request, pk, format=None):
        return Response({'msg': 'test'}, status=status.HTTP_200_OK)
'''

from users.serializers import UserSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework import viewsets


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
        # 获取token
        token = response.data.get('token', '')

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


# 用户视图
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

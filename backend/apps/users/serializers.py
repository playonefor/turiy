from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import tGroup

User = get_user_model()


# 用户列表序列化
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = (
            'id', 'username', 'name', 'mobile',
            'wechat', 'email', 'is_active', 'is_staff',
            'last_login', 'password', 'tgroup'
        )
        extra_kwargs = {'password': {'write_only': True}}
        # fields = "__all__"


# 用户组下用户序列化
class tGroupUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = (
            'id', 'name', 'username'
        )


# 用户组列表序列化
class tGroupListSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = tGroup
        fields = (
            'id', 'name', 'date_created', 'comment'
        )


# 用户组详情序列化
class tGroupDetailSerializer(serializers.ModelSerializer):

    users = tGroupUserSerializer(many=True)

    class Meta(object):
        model = tGroup
        fields = (
            'id', 'name', 'comment', 'date_created', 'users'
        )


# 用户组创建序列化
class tGroupCreateSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = tGroup
        fields = (
            'id', 'name', 'comment', 'users'
        )

    def create(self, validated_data):
        users_data = validated_data.pop('users')
        instance = tGroup.objects.create(**validated_data)
        for user in users_data:
            instance.users.add(user)
        return instance

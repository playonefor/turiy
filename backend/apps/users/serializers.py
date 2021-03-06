from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import tGroup
from application.models import Application
from perm.models import PerMisson

User = get_user_model()


# 应用序列化
class AppSimpleSerilizer(serializers.ModelSerializer):
    envcode = serializers.CharField(source='get_env_display')

    class Meta(object):
        model = Application
        fields = (
            'id', 'name', 'env', 'envcode'
        )


# 权限序列化
class PermSimpleSerializer(serializers.ModelSerializer):
    apps = AppSimpleSerilizer(many=True)

    class Meta(object):
        model = PerMisson
        fields = (
            'id', 'name', 'apps'
        )


# 用户基本字段序列化
class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'name'
        )


# 用户列表序列化
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'name', 'mobile',
            'wechat', 'email', 'is_active', 'is_staff',
            'last_login', 'password', 'tgroup'
        )
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}
        # fields = "__all__"

    def update(self, instance, validated_data):
        instance = super(UserSerializer, self).update(instance, validated_data)
        if validated_data.get("password", ""):
            instance.set_password(validated_data.get("password"))
        instance.save()
        return instance


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'name', 'mobile',
            'wechat', 'email', 'is_active', 'is_staff',
            'password', 'tgroup'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


# 用户组下用户序列化
class tGroupUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = (
            'id', 'name', 'username'
        )


# 用户组列表序列化
class tGroupListSerializer(serializers.ModelSerializer):

    users = tGroupUserSerializer(many=True)

    class Meta(object):
        model = tGroup
        fields = (
            'id', 'name', 'date_created', 'comment', 'users'
        )


# 用户组详情序列化
class tGroupDetailSerializer(serializers.ModelSerializer):

    users = tGroupUserSerializer(many=True)

    class Meta(object):
        model = tGroup
        fields = (
            'id', 'name', 'comment', 'date_created', 'users'
        )

    def update(self, instance, validated_data):
        print(validated_data)
        instance = super(tGroupDetailSerializer, self).update(instance, validated_data)
        print(instance.users)
        return instance


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


# 用户组更新序列化
class tGroupUpdateSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = tGroup
        fields = (
            'id', 'name', 'comment', 'users'
        )


# 用户组详情序列化
class tGroupPermAppDetailSerializer(serializers.ModelSerializer):
    perms = PermSimpleSerializer(source='granted_by_permissions', many=True)

    class Meta(object):
        model = tGroup
        fields = (
            'id', 'name', 'perms'
        )

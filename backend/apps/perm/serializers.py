from rest_framework import serializers
from perm.models import PerMisson
from users.models import UserProfile, tGroup
from application.models import Application


# 用户序列化
class PermUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = UserProfile
        fields = (
            'id', 'username', 'name'
        )


# 用户组序列化
class PermtGroupSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = tGroup
        fields = (
            'id', 'name'
        )


# 应用序列化
class PermAppSerializer(serializers.ModelSerializer):
    env = serializers.CharField(source='get_env_display')

    class Meta(object):
        model = Application
        fields = (
            'id', 'name', 'env'
        )


# 权限列表序列化
class PermListSerializer(serializers.ModelSerializer):
    apps = PermAppSerializer(many=True)
    users = PermUserSerializer(many=True)
    tgroups = PermtGroupSerializer(many=True)

    class Meta(object):
        model = PerMisson
        fields = (
            'id', 'name', 'date_created', 'comment', 'apps', 'users', 'tgroups'
        )


# 权限简单列表序列化
class PermListSimpleSerializer(serializers.ModelSerializer):
    apps = PermAppSerializer(many=True)

    class Meta(object):
        model = PerMisson
        fields = (
            'id', 'name', 'apps'
        )


# 权限详情序列化
class PermDetailSerializer(serializers.ModelSerializer):
    apps = PermAppSerializer(many=True)
    users = PermUserSerializer(many=True)
    tgroups = PermtGroupSerializer(many=True)

    class Meta(object):
        model = PerMisson
        fields = (
            'id', 'name', 'apps', 'users',
            'tgroups', 'date_created', 'comment'
        )


# 权限创建序列化
class PermCreateSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = PerMisson
        fields = (
            'id', 'name', 'apps', 'users',
            'tgroups', 'comment'
        )

    def create(self, validated_data):
        users = validated_data.pop('users')
        tgroups = validated_data.pop('tgroups')
        apps = validated_data.pop('apps')

        instance = PerMisson.objects.create(**validated_data)

        for user in users:
            instance.users.add(user)

        for app in apps:
            instance.apps.add(app)

        for tgroup in tgroups:
            instance.tgroups.add(tgroup)

        return instance


# 权限更新序列化
class PermUpdateSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = PerMisson
        fields = (
            'id', 'name', 'apps', 'users', 'tgroups', 'comment'
        )

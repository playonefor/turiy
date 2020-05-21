from rest_framework import serializers
from application.models import Application


# 应用列表序列化
class ApplicationListSerializer(serializers.ModelSerializer):
    env = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = (
            'id', 'name', 'env', 'comment'
        )

    def get_env(self, obj):
        return obj.get_env_display()


# 应用列表详情序列化
class ApplicationDetailSerializer(serializers.ModelSerializer):
    env = serializers.CharField(source='get_env_display')

    class Meta:
        model = Application
        fields = (
            'id', 'name', 'env', 'comment'
        )


# 应用创建序列化
class ApplicationCreateSerializer(serializers.ModelSerializer):
    env = serializers.ChoiceField(choices=Application.ENV)

    class Meta:
        model = Application
        fields = (
            'name', 'env', 'comment'
        )

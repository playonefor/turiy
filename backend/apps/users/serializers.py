from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('username', 'name', 'mobile', 'wechat', 'email', 'is_active', 'is_staff')



# Create your views here.




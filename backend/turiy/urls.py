"""turiy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from apps.users.views import CustomObtainJSONWebToken
from rest_framework import routers
from apps.rental import views as rental_views
from apps.users import views as user_views

router = routers.DefaultRouter()
router.register(r'friends', rental_views.FriendViewset)
router.register(r'belongings', rental_views.BelongingViewset)
router.register(r'borrowings', rental_views.BorrowedViewset)
router.register(r'users', user_views.UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/login/', CustomObtainJSONWebToken.as_view()),
    path('api/v1/', include(router.urls)),
]

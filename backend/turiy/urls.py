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

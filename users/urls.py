from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (PaymentViewSet, UserCreateAPIView, UserDestroyAPIView, UserListAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('user_list/', UserListAPIView.as_view(), name='user_list'),
    path('user_detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user_delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]

urlpatterns += router.urls

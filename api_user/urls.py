from django.urls import path
from .views import CustomUserListAPIView, CustomUserDetailAPIView

app_name = 'api_user'
urlpatterns = [
    path('users/', CustomUserListAPIView.as_view(), name='users'),
    path('users/<int:pk>/', CustomUserDetailAPIView.as_view(), name='user-detail'),

]
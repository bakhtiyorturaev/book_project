from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'password', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active',
                  'phone_number', 'image_user', 'groups', 'user_permissions']



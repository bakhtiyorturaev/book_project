from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from users.models import CustomUser
from .serializer import CustomUserSerializer


# Create your views here.


class CustomUserListAPIView(APIView):
    def get(self, request):
        user = CustomUser.objects.all()
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(user, request)
        serializer = CustomUserSerializer(page_obj, many=True)
        return paginator.get_paginated_response(data=serializer.data)


class CustomUserDetailAPIView(APIView):
    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(user)
        return Response(data=serializer.data)


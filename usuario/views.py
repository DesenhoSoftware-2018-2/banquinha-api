from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import serializers
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests, json
from .models import Profile
from .serializers import UserSerializer
from .serializers import ProfileSerializer


@api_view(['GET'])
@permission_classes((AllowAny,))
def get(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_serialization = serializers.serialize('json', list(users))
        if not users:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'usuarios': UserSerializer(users, many=True).data})

@api_view(['POST'])
@permission_classes((AllowAny,))
def post(request):
    if request.method == 'POST':
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

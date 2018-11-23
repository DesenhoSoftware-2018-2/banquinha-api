from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.utils.decorators import method_decorator
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
        if not users:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'usuarios': UserSerializer(users, many=True).data})

@api_view(['GET'])
@permission_classes((AllowAny,))
def getprofile(request):
    if request.method == 'GET':
        users = Profile.objects.all()
        user_serialazed = ProfileSerializer(users, many=True).data
        if not users:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'usuarios': user_serialazed})

@api_view(['POST'])
@permission_classes((AllowAny,))
def post(request):
    if request.method == 'POST':
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            print('is_valid')
            print(serialized.save())
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', ])
def login_view(request) :
    if request.method == 'PUT':

        email = request.data['email']
        password = request.data['password']
        print(email)
        print(password)
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print('primeiro')
            return Response(status=status.HTTP_200_OK)
        else:
            print('segundo')
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


#@api_view(['PUT', 'GET'])
#@method_decorator(csrf_protect)
#def login_view(self, request, format=None):
#    data = request.data
#    email = data.get('email', None)
#    password = data.get('password', None)
#    user = authenticate(email=email, password=password)
#    if user is not None:
#        if user.is_active:
#            log(request, user)
#
#            return Response(status=status.HTTP_200_OK)
#        else:
#            return Response(status=status.HTTP_404_NOT_FOUND)
#    else:
#        return Response(status=status.HTTP_404_NOT_FOUND)

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import serializers
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json
from .models import UserProfile
from .serializers import UserProfileSerializer
from .serializers import UserSerializer


@api_view(['GET'])
def get(request):
    #method to GET all users from API
    if request.method == 'GET':
        users = User.objects.all()
        user_serialization = serializers.serialize('json', list(users))
        if not users:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'usuarios': UserSerializer(users, many=True).data})

@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(request.POST, instance=request.user)
        #userProfile_serializer = UserProfileSerializer(request.POST, instance=request.user.profile)
        if user_serializer.is_valid():
            user_serializer.save()
            #userProfile_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

#@api_view(['POST'])
#@permission_classes((AllowAny,))
#def post(request):
#    if request.method == 'POST':
#        import ipdb; ipdb.set_trace()
#        serialized = UserSerializer(data=request.data)
#        if serialized.is_valid():
#            serialized.save()
#            return Response(serialized.data, status=status.HTTP_201_CREATED)
#        else:
#            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

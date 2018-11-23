from django.shortcuts import render
from .models import Monitoria, Tag, Profile
from django.contrib.auth.models import User
from .serializers import MonitoriaSerializer, TagSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests, json

@api_view(['GET', 'POST'])
def monitoria(request):

    if request.method == 'GET':
        monitoria = Monitoria.objects.all()
        if not monitoria:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(MonitoriaSerializer(monitoria, many=True).data)

    elif request.method == 'POST':
        if request.data:
            user = User.objects.get(id=request.data['mentor'])
            mentor = Profile.objects.get(user=user)
            print(mentor)
            monitoria, created = Monitoria.objects.get_or_create(                
                name = request.data['name'],
                date = request.data['date'],
                image = request.data['image'],
                content = request.data['content'],
                mentor = mentor,
            )            

            if created:                
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def tag(request):

    if request.method == 'GET':
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        return JsonResponse(serializer.data, safe=False)
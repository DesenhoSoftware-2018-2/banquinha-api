from django.shortcuts import render
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests, json

@api_view(['GET'])
def getUsuario(request):
    #method to GET all users from API
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createUsuario(request):
    if request.method == 'POST':

        if request.data:
            usuario, created = Usuario.objects.get_or_create(
                nome = request.data['nome'],
                email = request.data['email'],
                senha = request.data['senha']
            )

            if created:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

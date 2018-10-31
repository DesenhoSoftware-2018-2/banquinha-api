from django.shortcuts import render
from .models import Monitoria
from .serializers import MonitoriaSerializer
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
        serializer = MonitoriaSerializer(monitoria, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        if request.data:
            monitoria, created = Monitoria.objects.get_or_create(
                nome = request.data['nome'],
                imagem = request.data['imagem'],
                tag = request.data['tag'],
                data = request.data['data'],
                hora = request.data['hora'],
                conteudo = request.data['conteudo']
            )

            if created:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

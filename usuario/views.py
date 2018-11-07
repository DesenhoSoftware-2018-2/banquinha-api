from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import serializers
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json
from .models import Usuario
from .serializers import UsuarioSerializer
import jwt as jwt


@api_view(['GET'])
def get(request):
    #method to GET all users from API
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        usuario_serialization = serializers.serialize('json', list(usuario))
        if not usuario:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse(usuario_serialization, safe=False)

@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        if request.data:
            usuarioAuth = User.objects.filter(email=request.data['email'])
            if len(usuarioAuth) > 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                nome = request.data['nome'].split(' ')
                FLAG = True
                lastName = ''
                for i in nome:
                    if not FLAG:
                        lastName += i + ' '
                    FLAG = False

                usuarioAuth = User.objects.create_user(
                    username = request.data['nome'],
                    email = request.data['email'],
                    password = request.data['senha'],
                    first_name = nome,
                    last_name = lastName
                )

                usuarioAuth.save()
                usuario, created = Usuario.objects.get_or_create(
                    usuario = usuarioAuth,
                    tokenUsuario = jwt.encode(
                        {'data': {
                            'nome': request.data['nome'],
                            'email': request.data['email'],
                            'senha': request.data['senha']
                            }
                        },
                        'secret', algorithm='HS256'
                    )
                )

                import ipdb; ipdb.set_trace()
                if created:
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_BAD_REQUEST)

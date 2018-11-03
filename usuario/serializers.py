from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.Serializer):
    nome = serializers.CharField()
    email = serializers.CharField()
    senha = serializers.CharField()
    #avaliacao = serializers.ReadOnlyField()

    class Meta:
        model = Usuario
        fields = (
            'nome',
            'email',
            'senha'
            #'avaliacaoFK'
        )

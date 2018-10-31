from .models import Monitoria
from rest_framework import serializers


class MonitoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monitoria
        fields = (
            'nome',
            'conteudo',
            'data',
            'hora',
            'imagem',
            'tag',)

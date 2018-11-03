from .models import Monitoria
from rest_framework import serializers


class MonitoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monitoria
        fields = (
            'mentor',
            'nome',
            'conteudo',
            'dataHora',
            'imagem',
            'tag',)

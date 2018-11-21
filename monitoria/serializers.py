from .models import Tag, Evento, Monitoria
from rest_framework import serializers


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'tag',)

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = (
            'nome',
            'data',
            'imagem',
            'conteudo')

class MonitoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monitoria
        fields = (
            'mentor')

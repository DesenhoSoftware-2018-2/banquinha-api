from .models import Tag, Event, Monitoria
from rest_framework import serializers


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'tag',)

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = (
            'name',
            'date',
            'image',
            'content',
            'mentor',)

class MonitoriaSerializer(serializers.HyperlinkedModelSerializer):
    mentor = serializers.SerializerMethodField()

    class Meta:
        model = Monitoria
        fields = (
            'name', 'date', 'image', 'content', 'tag', 'mentored', 'mentor', )

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
        tag = serializers.ReadOnlyField()
        mentor = serializers.ReadOnlyField()
        fields = (
            'name',
            'date',
            'image',
            'content',
            'tag',
            'mentored',
            'mentor',)

class MonitoriaSerializer(serializers.HyperlinkedModelSerializer):
    mentor = serializers.SerializerMethodField()
    
    class Meta:
        model = Monitoria
        fields = (
            'name',
            'date',
            'image',
            'content',
            'tag',
            'mentored',
            'mentor',
            'max_mentorado',)

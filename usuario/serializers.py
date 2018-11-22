from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name'
        )

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            'user',
            'description',
            'achievement'
        )

    def get_user(self, obj):
        "obj is a Member instance. Returns list of dicts"""
        qset = User.objects.filter(user=obj)
        user_serialized = [UserSerializer(m).data for m in qset]
        return user_serialized[0]

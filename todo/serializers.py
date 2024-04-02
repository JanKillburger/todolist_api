from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Todo
        fields = ['created_at', 'title', 'description', 'user']

from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['created_at', 'title', 'description'] #, 'user']

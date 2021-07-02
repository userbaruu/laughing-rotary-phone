from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['user']
        read_only_fields = ['created', 'datecompleted']


class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['user']
        read_only_fields = ['title', 'memo', 'created', 'important', 'datecompleted']

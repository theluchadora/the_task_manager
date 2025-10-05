from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'user', 'completed_at']
        read_only_fields = ['user', 'completed_at']

    def validate_due_date(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("Due date must be in the future")
        return value
    

    def validate(self, data):
        if self.instance and self.instance.status == 'Completed' and data.get('status') != 'Pending':
            raise serializers.ValidationError("Completed tasks can't be edited unless reverted to pending")
        return data
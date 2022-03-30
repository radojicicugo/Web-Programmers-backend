from django.forms import fields
from rest_framework import serializers
from .models import Api

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = '__all__'
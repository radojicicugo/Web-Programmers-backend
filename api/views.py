from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Api 
from .serializers import ApiSerializer
from rest_framework import viewsets
# Create your views here.


class ApiView(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
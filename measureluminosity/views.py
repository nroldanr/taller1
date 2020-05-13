from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import LumSensor
from .serializers import LumSensorSerializer

class LumSensorViewSet(viewsets.ModelViewSet):
    queryset = LumSensor.objects.all().order_by('-created')
    serializer_class = LumSensorSerializer
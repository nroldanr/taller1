from rest_framework import serializers
from .models import LumSensor

class LumSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LumSensor
        fields = ('id', 'type', 'value','latitud','longitud','tipoDeTerreno')
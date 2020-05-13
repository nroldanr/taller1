from django.db import models

# Create your models here.
import uuid

class LumSensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    latitud = models.CharField(verbose_name='latitud', max_length=20)
    longitud = models.CharField(verbose_name='longitud', max_length=20)
    tipoDeTerreno = models.CharField(verbose_name='TipoDeTerreno', max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
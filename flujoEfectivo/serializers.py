from dataclasses import fields
from rest_framework import routers, serializers, viewsets

#importacion do modelos

from flujoEfectivo.models import FlujoEfec

class FlujoEfecSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlujoEfec
        fields = ('pk','fecha','descripcion','tipo_flujo','categoria')

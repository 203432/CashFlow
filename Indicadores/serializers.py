from rest_framework import  serializers

#importacion do modelos

from Indicadores.models import tableIndi

class indicadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model =   tableIndi
        fields = ('pk','indicador','numSemana','monto', 'Razon')

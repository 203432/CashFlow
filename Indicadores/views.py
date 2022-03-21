from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import exceptions
import os.path
from pathlib import Path

# importaciones de modelos agregados
from Indicadores.models import tableIndi

# importaciones de serializadores
from Indicadores.serializers import indicadoresSerializer

# Create your view here.

class indicadoresList(APIView):
    def get(self, request, format=None):
        queryset = tableIndi.objects.all()
        serializer = indicadoresSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = indicadoresSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            # Convertir y guardar el modelo
            flujo = tableIndi(**validated_data)
            flujo.save()
            serializer_response = indicadoresSerializer(flujo)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class indicadoresDetail(APIView):
     def get_object(self, pk):
         try:
             return tableIndi.objects.get(pk = pk)
         except tableIndi.DoesNotExist:
             return 0

     def get(self, request,pk, format=None):
         idResponse = self.get_object(pk)
         if idResponse != 0:
             idResponse = indicadoresSerializer(idResponse)
             return Response(idResponse.data, status = status.HTTP_200_OK)
         return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)

     def put(self, request,pk, format=None):
         idResponse = self.get_object(pk)
         serializer = indicadoresSerializer(idResponse, data = request.data)
         if serializer.is_valid():
             serializer.save()
             datas = serializer.data
             return Response(datas, status = status.HTTP_201_CREATED)
         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)



class IndicadorCobrar(generics.ListAPIView):
     def get(self, request, format=None):
         queryset = tableIndi.objects.filter(indicador="Cobrar")
         serializer = indicadoresSerializer(queryset, many = True, context = {'request':request})
         return Response(serializer.data, status=status.HTTP_200_OK)

class IndicadorPagar(generics.ListAPIView):
     def get(self, request, format=None):
         queryset = tableIndi.objects.filter(indicador="Pagar")
         serializer = indicadoresSerializer(queryset, many = True, context = {'request':request})
         return Response(serializer.data, status=status.HTTP_200_OK)
class IndicadorBanco(generics.ListAPIView):
     def get(self, request, format=None):
         queryset = Categoria.objects.filter(tipo="Salida")
         serializer = CategoriaSerializer(queryset, many = True, context = {'request':request})
         return Response(serializer.data, status=status.HTTP_200_OK)

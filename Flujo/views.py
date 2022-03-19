from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os.path
from pathlib import Path

# importaciones de modelos agregados
from categorias.models import Categoria
from Flujo.models import FlujoEfec

# importaciones de serializadores
from Flujo.serializers import FlujoEfecSerializer

# Create your view here.

class FlujoEfecList(APIView):
    def get(self, request, format=None):
        queryset = FlujoEfec.objects.all()
        serializer = FlujoEfecSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = FlujoEfecSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            # Convertir y guardar el mo
            # delo
            flujo = FlujoEfec(**validated_data)
            flujo.save()
            serializer_response = FlujoEfecSerializer(flujo)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FlujoEfecDetail(APIView):
     def get_object(self, pk):
         try:
             return FlujoEfec.objects.get(pk = pk)
         except FlujoEfec.DoesNotExist:
             return 0

     def get(self, request,pk, format=None):
         idResponse = self.get_object(pk)
         if idResponse != 0:
             idResponse = FlujoEfecSerializer(idResponse)
             return Response(idResponse.data, status = status.HTTP_200_OK)
         return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)

     def put(self, request,pk, format=None):
         idResponse = self.get_object(pk)
         serializer = FlujoEfecSerializer(idResponse, data = request.data)
         if serializer.is_valid():
             serializer.save()
             datas = serializer.data
             return Response(datas, status = status.HTTP_201_CREATED)
         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

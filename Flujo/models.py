from django.db import models
from django.utils import timezone
from categorias.models import Categoria
from datetime import datetime, date

# Create your models here.

class FlujoEfec(models.Model):
    fecha= models.DateField(auto_now_add=True)
    descripcion=models.CharField(max_length=100, null=False)
    tipo_flujo=models.CharField(max_length=50, null=False)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad=models.IntegerField(null=False)

    
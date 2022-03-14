from django.db import models
from django.utils import timezone
from categorias.models import Categoria

# Create your models here.

class FlujoEfec(models.Model):
    fecha= models.DateTimeField(default=timezone.now)
    descripcion=models.CharField(max_length=100, null=False)
    tipo_flujo=models.CharField(max_length=50, null=False)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    

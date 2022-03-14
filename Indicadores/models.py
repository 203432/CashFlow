from ast import Num
from django.db import models
# Create your models here.

class tableIndi(models.Model):
    indicador=models.CharField(max_length=100, null=False)
    numSemana=models.IntegerField(null=False)
    Razon=models.CharField(max_length=50, null=False)
    monto=models.IntegerField(null=False)


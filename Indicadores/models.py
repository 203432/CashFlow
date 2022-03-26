from ast import Num
from django.db import models
from datetime import datetime, date
# Create your models here.

class tableIndi(models.Model):
    fecha= models.DateField(auto_now_add=True, unique=False)
    indicador=models.CharField(max_length=100, null=False)
    numSemana=models.IntegerField(null=False)
    semana1 =  models.FloatField(null=False)
    semana2 = models.FloatField(null=False)
    semana3 = models.FloatField(null=False)
    semana4 = models.FloatField(null=False)
    semana5 = models.FloatField(null=False, default=0)
    Razon=models.CharField(max_length=50, null=False, unique=True)
    monto=models.FloatField(null=False)
    mes = models.CharField(max_length=50, null=False, default= datetime.today().month) 


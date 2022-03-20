from ast import Num
from django.db import models
# Create your models here.

class tableIndi(models.Model):
    fecha= models.DateField(auto_now_add=True, unique=False)
    indicador=models.CharField(max_length=100, null=False)
    numSemana=models.IntegerField(null=False)
    Razon=models.CharField(max_length=50, null=False)
    monto=models.IntegerField(null=False)

    @property
    def only_month(self):
        return self.fecha.strftime('%m')


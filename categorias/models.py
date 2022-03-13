from django.db import models

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50, null=False)
    clasificacion = models.CharField(max_length=50, null=False)

    class Meta:
        managed: True
        db_table: 'Categoria'


# Create your models here.

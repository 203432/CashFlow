# Generated by Django 4.0.1 on 2022-03-14 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indicadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableindi',
            name='numSemana',
            field=models.IntegerField(max_length=50),
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-20 05:48

import calendar
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flujo', '0002_rename_categoria_flujoefec_id_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flujoefec',
            name='fecha',
            field=models.DateField(auto_now_add=True, unique=calendar.TextCalendar.formatmonth),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessiones', '0008_alter_reservaciones_fecha_reservacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessiones',
            name='duracion',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sessiones',
            name='fecha_fin',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='sessiones',
            name='fecha_inicio',
            field=models.DateTimeField(null=True),
        ),
    ]

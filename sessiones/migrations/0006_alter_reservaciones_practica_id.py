# Generated by Django 4.2.6 on 2023-10-30 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practicas', '0001_initial'),
        ('sessiones', '0005_alter_reservaciones_practica_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaciones',
            name='practica_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practicas.practicas'),
        ),
    ]

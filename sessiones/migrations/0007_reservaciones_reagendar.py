# Generated by Django 4.2.6 on 2023-11-02 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessiones', '0006_alter_reservaciones_practica_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservaciones',
            name='reagendar',
            field=models.BooleanField(default=True),
        ),
    ]

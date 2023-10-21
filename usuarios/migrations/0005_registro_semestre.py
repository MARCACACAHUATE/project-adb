# Generated by Django 4.2.6 on 2023-10-19 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_role_role_delete_registro_semestre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_final', models.DateTimeField()),
                ('alumno_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 4.2.6 on 2023-10-27 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_usuarios_grupos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='grupos',
        ),
    ]

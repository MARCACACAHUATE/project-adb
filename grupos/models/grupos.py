from django.db import models

class Grupos(models.Model):
    id = models.AutoField(primary_key=True)
    numero_brigada = models.CharField(max_length=10, null=False)
    maestro_id = models.ForeignKey(
        "usuarios.Usuarios", 
        on_delete=models.SET_NULL, 
        related_name="maestro_id",
        null=True
    )
    alumnos = models.ManyToManyField(
        "usuarios.Usuarios", 
        related_name="alumnos"
    )
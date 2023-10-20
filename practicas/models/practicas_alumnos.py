from django.db import models
from django.utils import timezone


class PracticasAlumnos(models.Model):
    fecha_entrega = models.DateTimeField(default=timezone.now)
    alumno_id = models.ForeignKey("usuarios.Usuarios", on_delete=models.CASCADE)
    practica_id = models.ForeignKey("practicas.Practicas", on_delete=models.CASCADE) 
    archivo = models.CharField(max_length=250, null=True)
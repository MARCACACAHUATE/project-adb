from django.db import models
from django.utils import timezone


class Reservaciones(models.Model):
    fecha_reservacion = models.DateTimeField()
    is_valid = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    alumno_id = models.ForeignKey("usuarios.Usuarios", on_delete=models.CASCADE)
    practica_id = models.ForeignKey("practicas.PracticasAlumnos", on_delete=models.CASCADE)
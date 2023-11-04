from django.db import models
from django.utils import timezone


class Reservaciones(models.Model):
    fecha_reservacion = models.DateTimeField(default=timezone.now)
    is_valid = models.BooleanField(default=True)
    reagendar = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    alumno_id = models.ForeignKey("usuarios.Usuarios", on_delete=models.CASCADE)
    practica_id = models.ForeignKey("practicas.Practicas", on_delete=models.CASCADE)
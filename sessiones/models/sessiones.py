from django.db import models


class Sessiones(models.Model):
    fecha_inicio = models.DateTimeField(null=True)
    fecha_fin = models.DateTimeField(null=True)
    duracion = models.CharField(max_length=10, null=True)
    is_active = models.BooleanField(default=True)
    reservacion_id = models.ForeignKey("sessiones.Reservaciones", on_delete=models.CASCADE)
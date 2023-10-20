from django.db import models

class Registro_Semestre(models.Model):
    alumno_id = models.ForeignKey("Usuarios", null=True, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True, null=False)
    fecha_inicio = models.DateTimeField(null=False)
    fecha_final = models.DateTimeField(null=False)
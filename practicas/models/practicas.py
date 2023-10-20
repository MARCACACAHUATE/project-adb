from django.db import models


class Practicas(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    is_valid = models.BooleanField(default=True)
    archivo = models.CharField(max_length=250, null=True)
    maestro_id = models.ForeignKey("usuarios.Usuarios", null=True, on_delete=models.SET_NULL)
    grupo_id = models.ForeignKey("grupos.Grupos", null=True, on_delete=models.SET_NULL)
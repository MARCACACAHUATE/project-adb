from django.db import models

class Grupos(models.Model):
    numero_brigada = models.CharField(max_length=10, null=False)
    maestro_id = models.ForeignKey("usuarios.Usuarios", on_delete=models.SET_NULL, null=True)
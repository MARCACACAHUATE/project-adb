from django.db import models

class Role(models.Model):
    Role = models.CharField(max_length=30, unique=True, null=True)


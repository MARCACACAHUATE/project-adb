from django.db import models

class Role(models.Model):
    role = models.CharField(max_length=30, unique=True, null=True)


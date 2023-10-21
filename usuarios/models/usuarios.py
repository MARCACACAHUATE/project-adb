from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from usuarios.managers import CustomUserManager

class Usuarios(AbstractBaseUser, PermissionsMixin):
    matricula = models.CharField(_("Matricula"), max_length=10, unique=True, null=False)
    nombre = models.CharField(max_length=100, null=False)
    correo = models.EmailField(_("Correo Universitario"), unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    cerated_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(null=True)

    role_id = models.ForeignKey(
        "Role", null=True,
        on_delete=models.CASCADE
    )

    USERNAME_FIELD = "matricula"
    REQUIRED_FIELDS = ["role_id"]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.nombre} {self.matricula}"
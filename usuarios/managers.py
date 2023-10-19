from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
#from .models import Role

class CustomUserManager(BaseUserManager):
    """
        Custom manger donde la matricula es el campo para la
        authentificacion
    """

    def create_user(self, matricula: str, password: str, **extra_fields):
        """
            Crea y guarda un usuario con la matricula y contraseña
        """
        if not matricula:
            raise ValueError(_("La matricula debe ser establecida"))

        user = self.model(matricula=matricula, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, matricula, password, **extra_fields):
        """
            Crea y guarda un SuperUser con la matricula y password dada.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(matricula, password, **extra_fields)
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from usuarios.models import Role


class CustomUserManager(BaseUserManager):
    """
        Custom manger donde la matricula es el campo para la
        authentificacion
    """

    def create_user(self, matricula: str, password: str, is_maestro=False, **extra_fields):
        """
            Crea y guarda un usuario con la matricula y contraseña
        """
        if not matricula:
            raise ValueError(_("La matricula debe ser establecida"))

        user = self.model(matricula=matricula, **extra_fields)
        user.set_password(password)

        if is_maestro:
            maestro_role = Role.objects.get(Role="Maestro")
            user.role_id = maestro_role

        if extra_fields.get("is_superuser") is not True:
            alumno_role = Role.objects.get(Role="Alumno")
            user.role_id = alumno_role

        user.save()
        return user
    
    def create_superuser(self, matricula, password, **extra_fields):
        """
            Crea y guarda un SuperUser con la matricula y password dada.
        """
        try: 
            admin_role = Role.objects.get(Role="Admin")
        except Exception:
            admin_role = Role.objects.create(Role="Admin")
            admin_role.save()

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role_id", admin_role)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(matricula, password, **extra_fields)
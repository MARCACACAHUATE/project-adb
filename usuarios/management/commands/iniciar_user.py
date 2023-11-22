from usuarios.models import Usuarios
from django.core.management.base import BaseCommand
from decouple import config


class Command(BaseCommand):
    help = "Inicialilza un admin user"

    def handle(self, *args, **options):
        matricula = config("MATRICULA")
        password = config("PASSWORD")

        user = Usuarios.objects.create_superuser(matricula=matricula, password=password)
        self.stdout.write(f"Admin creado matricula {matricula} password {password}", self.style.SUCCESS)
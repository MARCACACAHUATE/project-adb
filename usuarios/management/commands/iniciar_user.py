from usuarios.models import Usuarios, Role
from django.core.management.base import BaseCommand
from decouple import config


class Command(BaseCommand):
    help = "Inicialilza un admin user"

    def handle(self, *args, **options):
        matricula = config("MATRICULA")
        password = config("PASSWORD")
        Role.objects.create(Role="Admin")
        Role.objects.create(Role="Maestro")
        Role.objects.create(Role="Alumno")

        user = Usuarios.objects.create_superuser(matricula=matricula, password=password)
        self.stdout.write(f"Admin creado matricula {matricula} password {password}", self.style.SUCCESS)
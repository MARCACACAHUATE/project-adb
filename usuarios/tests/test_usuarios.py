from django.test import TestCase
from usuarios.models import Usuarios, Role

class CreateUserWithRoleTestCase(TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        self.matricula_test = "123456789"
        super().__init__(methodName)

    def setup(self):

        Role.objects.create(Role="Maestro")
        Role.objects.create(Role="Alumno")
        Role.objects.create(Role="Admin")

    def test_create_user_maestro(self):
        Usuarios.objects.create_user(
            matricula=self.matricula_test,
            password="test_password",
            is_maestro=True
        )

        maestro_user = Usuarios.objects.get(matricula=self.matricula_test)
        maestro_role = Role.objects.get(Role="Maestro")

        self.assertEqual(maestro_user.role_id, maestro_role)

    def test_create_user_alumno(self):
        Usuarios.objects.create_user(
            matricula=self.matricula_test,
            password="test_password",
        )

        alumno_user = Usuarios.objects.get(matricula=self.matricula_test)
        alumno_role = Role.objects.get(Role="Alumno")

        self.assertEqual(alumno_user.role_id, alumno_role)

    def test_create_user_admin(self):
        Usuarios.objects.create_superuser(
            matricula=self.matricula_test,
            password="test_password",
        )

        admin_user = Usuarios.objects.get(matricula=self.matricula_test)
        admin_role = Role.objects.get(Role="Admin")

        self.assertEqual(admin_user.role_id, admin_role)
from django.shortcuts import render
from django.views import View

from practicas.models import Practicas  # Asegúrate de importar el modelo correcto
from usuarios.models import Usuarios
class ListPracticasView(View):
    template_name = "practicas.html"

    def get(self, request, *args, **kwargs):

        if request.session.get("role") == "Admin":
            lista_practicas = Practicas.objects.filter(
                practica_id = Usuarios.objects.get(pk=request.user.id)
            )
        else:
            lista_practicas = PracticasAlumnos.objects.all()

        print(lista_practicas)

        return render(request, self.template_name, { "lista_practicas": lista_practicas })

from django.shortcuts import render
from django.views import View
from grupos.models import Grupos
from practicas.models import PracticasAlumnos
from practicas.models.practicas import Practicas
from usuarios.models import Usuarios


class ListaPracticasView(View):
    template_name = "AlumnoInicio.html"

    def get(self, request, *args, **kwargs):
             if request.user.is_authenticated:
                usuario_id = request.user.id
                #alumno = Usuarios.objects.get(pk=self.kwargs["alumno_id"])
                #practica = Practicas.objects.get(pk=self.kwargs["practica_id"]) 
                print(usuario_id)
                print(PracticasAlumnos)
             return render(request, "AlumnoInicio.html")

        
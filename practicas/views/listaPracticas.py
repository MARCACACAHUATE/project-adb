from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from grupos.models import Grupos
from practicas.models import PracticasAlumnos
from practicas.models.practicas import Practicas
from usuarios.models import Usuarios
from grupos.models import Grupos


class ListaPracticasView(LoginRequiredMixin, View):
    login_url = "login/"
    template_name = "ListPracticas.html"

    def get(self, request, *args, **kwargs):
        grupo_id = self.kwargs["grupo_id"]
        grupo = Grupos.objects.get(pk=grupo_id)

        grupo_data = {
            "grupo_id": grupo_id,
            "numero_brigada": grupo.numero_brigada
        }
        practicas_list = Practicas.objects.filter(grupo_id=grupo)

        return render(request, self.template_name, {
            "grupo_data": grupo_data,
            "practicas_list": practicas_list
        })

        
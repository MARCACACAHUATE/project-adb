from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from practicas.models import Practicas


class DetailPracticasView(LoginRequiredMixin, View):
    login_url = "login/"
    template_name = "DetailPractica.html"

    def get(self, request, *args, **kwargs):

        practica = Practicas.objects.get(pk=self.kwargs["practica_id"])
        practica_data = {
            "id": practica.id,
            "titulo": practica.titulo,
            "descripcion": practica.descripcion,
            "fecha_inicio": practica.fecha_inicio,
            "fecha_fin": practica.fecha_fin
        }

        return render(request, self.template_name, { 
            "practica_id": self.kwargs["practica_id"],
            "practica": practica_data,
            "grupo_id": self.kwargs["grupo_id"]
        })
    
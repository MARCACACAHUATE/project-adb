from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

class DetallesAlumnoGrupoView(LoginRequiredMixin, View):
    login_url = "login/"
    template_name = "GrupoDetallesAlumno.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        pass
from django.shortcuts import render, redirect
from django.views import View
from grupos.forms import CreateGrupoForm
from usuarios.models import Usuarios, Role
from grupos.models import Grupos


class CreateGrupoView(View):
    form_class = CreateGrupoForm
    template_name = "CrearGrupo.html"

    def get(self, request, *args, **kwargs):
        maestros_list = Usuarios.objects.filter(role_id__Role="Maestro")
        return render(request, self.template_name, {"maestros_list": maestros_list})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print(request.POST["numero_brigada"])
            print(request.POST["maestro_id"])
            maestro = Usuarios.objects.get(pk=int(request.POST["maestro_id"]))
            Grupos.objects.create(
                numero_brigada=request.POST["numero_brigada"],
                maestro_id=maestro
            )
            return redirect("grupos:list")

        return redirect("grupos:list")
        
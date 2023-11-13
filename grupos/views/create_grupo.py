from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.views import View
from grupos.forms import CreateGrupoForm
from usuarios.models import Usuarios, Role
from grupos.models import Grupos
from practicas.models import Practicas


class CreateGrupoView(View):
    form_class = CreateGrupoForm
    template_name = "CrearGrupo.html"

    def get(self, request, *args, **kwargs):
        maestros_list = Usuarios.objects.filter(role_id__Role="Maestro")
        return render(request, self.template_name, {"maestros_list": maestros_list})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            data = form.cleaned_data    

            maestro = Usuarios.objects.get(pk=int(request.POST["maestro_id"]))
            grupo = Grupos.objects.create(
                numero_brigada=request.POST["numero_brigada"],
                maestro_id=maestro
            )

            if(data["gen_practicas"]):
                self.gen_practicas(grupo, maestro)

            return redirect("grupos:list")
        else:
            return render(request, self.template_name, {"mensaje": "Formulario Inválido"})

        return redirect("grupos:list")
        
    def gen_practicas(self, grupo, maestro):
        fecha_inicial = datetime.today()
        fecha_final = datetime.today() + timedelta(days=6)

        for practica_number in range(1, 11):

            Practicas.objects.create(
                titulo = f"Práctica {practica_number}",
                fecha_inicio = fecha_inicial,
                fecha_fin = fecha_final,
                maestro_id = maestro,
                grupo_id = grupo
            )

            fecha_inicial = fecha_inicial + timedelta(days=7)
            fecha_final = fecha_final + timedelta(days=7)
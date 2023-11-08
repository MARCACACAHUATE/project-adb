from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from grupos.models import Grupos
from usuarios.models.usuarios import Usuarios
from practicas.models import Practicas
from practicas.forms import CreatePracticasForm
from django.core.exceptions import ObjectDoesNotExist

class CreatePracticasView(LoginRequiredMixin, View):
    login_url = "login/"
    form_class = CreatePracticasForm
    template_name = "CreatePractica.html"

    def get(self, request, *args, **kwargs): 
        grupo_id = self.kwargs["grupo_id"]
        form = self.form_class()
        grupo = Grupos.objects.get(pk=grupo_id)
        grupo_data = {
            "grupo_id": grupo.id,
            "brigada": grupo.numero_brigada
        }

        return render(request, self.template_name, {
            'form': form,
            'grupos': grupo,
            'grupo_data': grupo_data
        })
    

    def post(self, request, *args, **kwargs):    
        form = CreatePracticasForm(request.POST)  
        grupo_id = self.kwargs["grupo_id"]
        grupo = Grupos.objects.get(pk=grupo_id)
        grupo_data = {
            "grupo_id": grupo.id,
            "brigada": grupo.numero_brigada
        }
        
        if form.is_valid():  
            try:
                cleaned_data = form.cleaned_data 
                maestro = Usuarios.objects.get(pk=request.session.get("user_id"))

                Practicas.objects.create(
                    titulo = cleaned_data["titulo"],
                    descripcion = cleaned_data["descripcion"],
                    fecha_inicio = cleaned_data["fecha_inicio"],
                    fecha_fin = cleaned_data["fecha_fin"],
                    maestro_id=maestro,
                    grupo_id=grupo
                ).save()

                return redirect("grupos:detail", grupo_id=grupo_id)

            except ObjectDoesNotExist:
                mensaje = "No se encontró el maestro o el grupo en la base de datos."
                return render(request, self.template_name, {
                    'form': form,
                    'grupos': grupo,
                    'grupo_data': grupo_data,
                    'mensaje': mensaje
                })
        else:
            print("Formulario NO valido")
            return render(request, self.template_name, {
                'form': form,
                'grupos': grupo,
                'grupo_data': grupo_data,
                'mensaje': "Formulario invalido"
            })
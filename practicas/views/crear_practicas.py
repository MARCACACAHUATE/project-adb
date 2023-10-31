from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from grupos.models.grupos import Grupos
from usuarios.models.usuarios import Usuarios
from practicas.models import Practicas
from practicas.forms import CreatePracticasForm
from django import forms


class CreatePracticasView(View):
    form_class = CreatePracticasForm
    template_name = "crearPracticas.html"

    def get(self, request, *args, **kwargs): 
        form = self.form_class()
        grupos = Grupos.objects.all()
        return render(request, self.template_name, {'form': form, 'grupos': grupos})
    

    def post(self, request, *args, **kwargs):    
        form = CreatePracticasForm(request.POST)  

        if form.is_valid():  
                    cleaned_data = form.cleaned_data 

        # Convierte el valor del campo 'is_valid' a un valor booleano
                    is_valid = cleaned_data.get("is_valid") == "on"

                    Practicas.objects.create(
                    titulo = request.POST["titulo"],
                    descripcion = request.POST["descripcion"],
                    fecha_inicio = request.POST["fecha_inicio"],
                    fecha_fin = request.POST["fecha_fin"],
                    is_valid = is_valid,
                    archivo = request.POST["archivo"],
                    #no supe como conectar las fk con la tabla, osea tal cual si se las pongo no puedo insertar
                   # maestro_id = request.POST["maestro_id"],
                   # grupo_id = request.POST["grupo_id"],
                    )
                    return HttpResponseRedirect('/crear_practicascopy/')
        else:
                return render(request, self.template_name, {'form': form})

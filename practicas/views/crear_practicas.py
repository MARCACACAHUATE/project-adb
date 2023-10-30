from django.shortcuts import render, redirect
from django.views import View
from grupos.models.grupos import Grupos
from usuarios.models.usuarios import Usuarios
from practicas.models import Practicas
from practicas.forms import CreatePracticasForm

class CreatePracticasView(View):
    form_class = CreatePracticasForm
    template_name = "grupos/templates/createPracticas.html"

    def get(self, request, *args, **kwargs): 
        grupos = Grupos.objects.all()
        return render(request, self.template_name, {'grupos': grupos})
    
 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)       
  
        print(request.POST["titulo"]) 
        print(request.POST["descripcion"]) 
        print(request.POST["fecha_inicio"]) 
        print(request.POST["fecha_fin"]) 
        print(request.POST["is_valid"]) 
        print(request.POST["archivo"]) 
        print(request.POST["maestro_id"]) 
        print(request.POST["grupo_id"]) 

        Practicas.objects.create(   
        titulo = request.POST["titulo"],
        descripcion = request.POST["descripcion"],
        fecha_inicio = request.POST["fecha_inicio"],
        fecha_fin = request.POST["fecha_fin"],
        is_valid = request.POST["is_valid"],
        archivo = request.POST["archivo"],
        maestro_id = request.POST["maestro_id"],
        grupo_id = request.POST["grupo_id"],
        )


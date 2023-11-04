from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from grupos.models import Grupos
from usuarios.models.usuarios import Usuarios
from practicas.models import Practicas
from practicas.forms import CreatePracticasForm
from django.core.exceptions import ObjectDoesNotExist

class CreatePracticasView(View):
    form_class = CreatePracticasForm
    template_name = "crearPracticas.html"

    def get(self, request, *args, **kwargs): 
        form = self.form_class()
        grupo = Grupos.objects.all()
        return render(request, self.template_name, {'form': form, 'grupos': grupo})
    

    def post(self, request, *args, **kwargs):    
        form = CreatePracticasForm(request.POST)  
        
        try:
                print(form.is_valid())
                print(request.POST)
                if form.is_valid():  
                    cleaned_data = form.cleaned_data 

                    isvalid = cleaned_data.get("is_valid") == "on"
                 
                    print(request.POST["maestro_id"])
                    print(request.POST["grupo_id"])

                    maestro = Usuarios.objects.get(pk=int(request.POST["maestro_id"]))
                    grupo= Grupos.objects.get(pk=int(request.POST["grupo_id"]))
            
                    Practicas.objects.create(
                    titulo = request.POST["titulo"],
                    descripcion = request.POST["descripcion"],
                    fecha_inicio = request.POST["fecha_inicio"],
                    fecha_fin = request.POST["fecha_fin"],
                    is_valid = isvalid,
                    archivo = request.POST["archivo"],
                    maestro_id=maestro,
                    grupo_id=grupo
                    ).save()

                mensaje = "Practica creada!"
                return HttpResponse(mensaje)
        except ObjectDoesNotExist:
                mensaje = "No se encontró el maestro o el grupo en la base de datos."
                return HttpResponse(mensaje)

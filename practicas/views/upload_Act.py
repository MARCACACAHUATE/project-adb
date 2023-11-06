from django.shortcuts import render, redirect
from django.views import View
from practicas.forms import UploadActForm # Importa el formulario correcto desde practicas.forms
from usuarios.models import Usuarios
from practicas.models import Practicas, PracticasAlumnos
from usuarios.models import Usuarios
from datetime import date
#import PyPDF2
from django.contrib.auth import authenticate
import os
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.conf import settings

class UploadActView(View):  # Cambia el nombre de la clase para evitar conflictos
    form_class = UploadActForm
    template_name = "subirPracticas.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
       
        #request.session["alumno_id"] = idUsuario.id.Usuarios
        #idUsuario = authenticate(request)
    
        if request.user.is_authenticated:
         usuario_id = request.user.id
        #alumno = Usuarios.objects.get(pk=self.kwargs["alumno_id"])
        #practica = Practicas.objects.get(pk=self.kwargs["practica_id"]) 
         print(usuario_id)
         print(PracticasAlumnos)
        else:
            message="q paso"
        #practica = Practicas.objects.get(pk=int(request.POST["practica_id"]))
        # Realiza las operaciones que necesites con los objetos alumno y practica
        #alumno = Usuarios.objects.all()
        #practica = Practicas.objects.all()

        #print(Usuarios.objects.all())
        #print(Practicas.objects.all())
        #print("ID del usuario logeado:", user_id)
        

        return render(request, self.template_name, {'form': form})
       
    def post(self, request, *args, **kwargs):
       
        fecha_entrega1 = datetime.now()
        #alumno = Usuarios.objects.get(pk=int(request.POST["alumno_id"]))
        #idUsuario=authenticate(request)
        #request.session["alumno_id"] = idUsuario.id
       
        #alumno = Usuarios.objects.get(pk=self.kwargs["alumno_id"])
        #practica = Practicas.objects.get(pk=self.kwargs["practica_id"]) 
       
        #print(idUsuario)
      
        #practica = Practicas.objects.get(pk=int(request.POST["1"]))
        #alumno = Usuarios.objects.get(pk=int(request.POST["1"]))


        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            practica= Practicas.objects.get(pk=int(request.POST["practica_id"])) 
            #usuario_id = request.user.id
            usuario_id = Usuarios.objects.get(pk=request.user.id)
            pdf_file = request.FILES["archivo"]
            pdf_upload_location = os.path.join(settings.MEDIA_ROOT, 'pdf_files')
            os.makedirs(pdf_upload_location, exist_ok=True)
            pdf_file_path = os.path.join(pdf_upload_location, pdf_file.name)

            with open(pdf_file_path, 'wb') as destination:
                for chunk in pdf_file.chunks():
                    destination.write(chunk)

                    PracticasAlumnos.objects.create(
                        fecha_entrega=fecha_entrega1,
                        alumno_id= usuario_id,
                        practica_id = practica,
                        #practica_id = practica,
                        archivo = pdf_upload_location
                    ).save()
                    mensaje = "Practica subida!"
                   

        else:
            form = self.form_class()

        return render(request, self.template_name)
    



   
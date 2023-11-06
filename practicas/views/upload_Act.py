from django.shortcuts import render, redirect
from django.views import View
from practicas.forms import UploadActForm 
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

class UploadActView(View): 
    form_class = UploadActForm
    template_name = "subirPracticas.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()

    
        if request.user.is_authenticated:
         usuario_id = request.user.id
         practicas = Practicas.objects.filter(usuario_id=user)

         print(usuario_id)
         print(PracticasAlumnos)
        else:
            message="q paso"
        

        return render(request, self.template_name, {'form': form})
       
    def post(self, request, *args, **kwargs):
       
        fecha_entrega1 = datetime.now()


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

                        archivo = pdf_upload_location
                    ).save()
                    mensaje = "Practica subida!"
                   

        else:
            form = self.form_class()

        return render(request, self.template_name)
    



   
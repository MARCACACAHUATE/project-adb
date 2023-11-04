"""""

from django.shortcuts import render, redirect
from django.views import View
from practicas.views import upload_Act
from usuarios.models import Usuarios
from practicas.models import Practicas


class upload_Act(View):
    form_class = upload_Act
    template_name = "subirPracticas.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        alumno = Usuarios.objects.get(pk=self.kwargs["alumno_id"])
        practica = Practicas.objects.get(pk=self.kwargs["practica_id"]) 
        print(Usuarios.alumnos.all())


   # def post(self, request, *args, **kwargs):

"""""
from django.shortcuts import render, redirect
from django.views import View
from practicas.forms import UploadActForm # Importa el formulario correcto desde practicas.forms
from usuarios.models import Usuarios
from practicas.models import Practicas, PracticasAlumnos

from datetime import date
#import PyPDF2

import os
from django.conf import settings


class UploadActView(View):  # Cambia el nombre de la clase para evitar conflictos
    form_class = UploadActForm
    template_name = "subirPracticas.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        #alumno = Usuarios.objects.get(pk=self.kwargs["alumno_id"])
        #practica = Practicas.objects.get(pk=self.kwargs["practica_id"])
        #alumno = Usuarios.objects.get(pk=int(request.POST["alumno_id"]))
        #practica = Practicas.objects.get(pk=int(request.POST["practica_id"]))
        # Realiza las operaciones que necesites con los objetos alumno y practica
        practicas= Practicas.objects.get(pk=self.kwargs["alumno_id"])
        print(practicas.objects.all())
        alumno = Usuarios.objects.get(pk=self.kwargs["practica_id"])
        print(alumno.objects.all())
        return render(request, self.template_name, {'form': form, 'alumno': alumno, 'practica': practicas})
       
    def post(self, request, *args, **kwargs):
       
        fecha_entrega = date.today()
        alumno = Usuarios.objects.get(pk=int(request.POST["alumno_id"]))
        practica = Practicas.objects.get(pk=int(request.POST["practica_id"]))
         #maestro = Usuarios.objects.get(pk=int(request.POST["maestro_id"]))
        # Ejemplo de cómo procesar un formulario válido:

        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # Realiza las operaciones necesarias para guardar los datos
            # Puedes acceder a los datos del formulario usando form.cleaned_data
            # Por ejemplo: alumno = Usuarios.objects.get(pk=form.cleaned_data['alumno_id'])
            # Y luego guardar la actividad en la base de datos
            # Luego, puedes redirigir a una página de éxito o donde desees.
            pdf_file = request.FILES["pdf_file"]

            # Obtén la ubicación donde deseas guardar los archivos PDF
            pdf_upload_location = os.path.join(settings.MEDIA_ROOT, 'pdf_files')

            # Asegúrate de que el directorio exista
            os.makedirs(pdf_upload_location, exist_ok=True)

            # Construye la ruta completa del archivo PDF
            pdf_file_path = os.path.join(pdf_upload_location, pdf_file.name)

            # Abre el archivo y guárdalo en la ubicación deseada
            with open(pdf_file_path, 'wb') as destination:
                for chunk in pdf_file.chunks():
                    destination.write(chunk)



            # Resto del código para procesar los datos del formulario y la base de datos
                    PracticasAlumnos.objects.create(
                        fecha_entrega=fecha_entrega,
                        alumno_id=alumno,
                        practica_id = practica,
                        archivo = pdf_file
                    ).save()
                    mensaje = "Practica subida!"
        else:
            form = self.form_class()

        return render(request, self.template_name)
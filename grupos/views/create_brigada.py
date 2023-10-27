import csv
import io
from datetime import date
from dateutil.relativedelta import relativedelta
#import requests
from django.shortcuts import render
from django.views import View
from grupos.forms import UploadCsvAlumnos
from usuarios.models import Usuarios, Registro_Semestre
from grupos.models import Grupos


class CreateBrigadaView(View):
    form_class = UploadCsvAlumnos
    template_name = "MaestroAltaBrigada.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        grupo = Grupos.objects.get(pk=self.kwargs["grupo_id"])
        return render(request, self.template_name, { 
            "form": form,
            "grupo": grupo
        })

    def post(self, request, *args, **kwargs):

        inicio_semestre = date.today()
        fin_semestre = inicio_semestre + relativedelta(months=+2)

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES["csv_file"]
            csv_file.seek(0)
            reader = csv.DictReader(io.StringIO(csv_file.read().decode('utf-8-sig')))

            for row in reader:
                alumno, created = Usuarios.objects.get_or_create(
                    matricula=row["matricula"]
                )

                Registro_Semestre.objects.create(
                    alumno_id=alumno,
                    fecha_inicio=inicio_semestre,
                    fecha_final=fin_semestre
                )
    
            return render(request, self.template_name)

        else:
            form = self.form_class()
        
        return render(request, self.template_name)

    def verify_alumnos(alumno):
        #response = requests.get()
        print("validando la chingadera")

#import requests
import csv
import io
import requests
from datetime import date, datetime
from typing import Any
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from grupos.forms import UploadCsvAlumnos
from usuarios.models import Usuarios, Registro_Semestre, Role
from grupos.models import Grupos


class CreateBrigadaView(LoginRequiredMixin, View):
    login_url = "login/"
    form_class = UploadCsvAlumnos
    template_name = "MaestroAltaBrigada.html"

    def get(self, request, *args, **kwargs):
        grupo = Grupos.objects.get(pk=self.kwargs["grupo_id"])

        #response = requests.get(f"http://127.0.0.1:36165/grupos/{grupo.numero_brigada}")

        #alumnos_siase: dict 
        #if response.status_code == 200:
        #    alumnos_siase = response.json()["alumnos"]
        #    print(alumnos_siase)

        alumnos = grupo.alumnos.all()
        lista_alumnos = self.map_alumnos_list(alumnos)
        return render(request, self.template_name, { 
            "form": self.form_class(),
            "grupo": grupo,
            "lista_alumnos": lista_alumnos
        })

    def post(self, request, *args, **kwargs):

        grupo = Grupos.objects.get(pk=self.kwargs["grupo_id"])


        inicio_semestre = date.today()
        fin_semestre = inicio_semestre + relativedelta(months=+2)

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES["csv_file"]
            csv_file.seek(0)
            reader = csv.DictReader(io.StringIO(csv_file.read().decode('utf-8-sig')))
            alumno_role = Role.objects.get(Role="Alumno")

            index = 1
            for row in reader:

                try:
                    # Validar los datos del csv
                    self.validate_csv_data(row, index)
                    
                    alumno, created = Usuarios.objects.get_or_create(
                        matricula=row["matricula"],
                        defaults= { "nombre": row["nombre"] }
                    )

                    if created:
                        alumno.role_id = alumno_role
                        Registro_Semestre.objects.create(
                            alumno_id=alumno,
                            fecha_inicio=inicio_semestre,
                            fecha_final=fin_semestre
                        )
                        alumno.save()
                        grupo.alumnos.add(alumno)
                        grupo.save()
                    else:
                        print(f"El alumno con matricula {alumno.matricula} ya fue creado")
                
                except KeyError as error:
                    error_message = "La estructura del archivo csv es incorrecto. Por favor seguir la estructura 'matricula, nombre' en minúscula"
                    lista_alumnos = grupo.alumnos.all()
                    return render(request, self.template_name, {
                        "error_message": error_message,
                        "form": form,
                        "grupo": grupo,
                        "lista_alumnos": lista_alumnos
                    })
                
                except ValueError as error:
                    error_message = error
                    lista_alumnos = grupo.alumnos.all()
                    return render(request, self.template_name, {
                        "error_message": error_message,
                        "form": form,
                        "grupo": grupo,
                        "lista_alumnos": lista_alumnos
                    })

                index+=1

    
            return redirect(f"/grupos/{self.kwargs['grupo_id']}")

        else:
            form = self.form_class()
        
        return render(request, self.template_name)

    def verify_alumnos(self, alumno):

        #response = requests.get(f"http://127.0.0.1:36165/grupos/{grupo.numero_brigada}")

        #alumnos_siase: dict = [] 
        #if response.status_code == 200:
        #    alumnos_siase = response.json()["alumnos"]
        #    print(alumnos_siase)

        print("validando alumnos")

    def validate_csv_data(self, csv_data: dict[str, str], index: int):
        # Valida tipo de dato correcto de la matricula
        matricula = csv_data["matricula"]
        if matricula.isdigit() is False:
            raise ValueError(f"La matrícula '{matricula}' del renglón {index} no es valida.")
        
        # Valida el size maximo de la matricula
        if len(matricula) > 10:
            raise ValueError(f"La matrícula del renglon {index} debe ser de 10 digitos como máximo.")
    
    def map_alumnos_list(self, lista_alumnos):

        alumnos_parsed = [{
            "id": alumno.id,
            "matricula": alumno.matricula,
            "nombre": alumno.nombre if alumno.nombre or len(alumno.nombre) > 0 else "Sin Nombre",
            "correo": alumno.correo if alumno.correo else "Sin Correo",
            "is_verified": alumno.is_verified,
            "is_active": alumno.is_active,
            "is_staff": alumno.is_staff,
            "cerated_at": alumno.cerated_at,
            "modified_at": alumno.modified_at,
            "role_id": alumno.role_id,
            "last_login": self.format_date(alumno.last_login) if alumno.last_login else "Sin Conexión"
        } for alumno in lista_alumnos]

        return alumnos_parsed

    # TODO: Refactorizar esta parte en una Clase base
    def format_date(self, date: datetime) -> str:
        month_index = date.month
        mes = { 
            1 :"enero",
            2 :"febrero",
            3: "marzo",
            4: "abril",
            5: "mayo",
            6: "junio",
            7: "julio",
            8: "agosto",
            9: "septiembre",
            10: "octubre",
            11: "noviembre",
            12: "diciembre",
        }

        return date.strftime(f"%d de {mes[month_index]} del %Y %H:%M")
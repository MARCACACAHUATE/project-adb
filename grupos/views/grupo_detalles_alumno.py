from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from sessiones.models import Sessiones, Reservaciones
from usuarios.models import Usuarios
from grupos.models import Grupos

class DetallesAlumnoGrupoView(LoginRequiredMixin, View):
    login_url = "login/"
    template_name = "GrupoDetallesAlumno.html"

    def get(self, request, *args, **kwargs):
        alumno = Usuarios.objects.get(pk=self.kwargs["alumno_id"])
        grupo = Grupos.objects.get(pk=self.kwargs["grupo_id"])
        reservaciones =  Reservaciones.objects.filter(alumno_id=alumno)
        sessions_list = []

        reservaciones_list = [ {
            "id": reservacion.id,
            "fecha_reservacion": self.format_date(reservacion.fecha_reservacion),
            "is_valid": "Valida" if reservacion.is_valid else "Invalida",
            "reagendar": "Reagendable" if reservacion.reagendar else "Ya ha reagendado",
            "created_at": reservacion.created_at,
            "alumno_id": reservacion.alumno_id,
            "practica_id": reservacion.practica_id
        } for reservacion in reservaciones ]

        for reservacion in reservaciones:

            sessiones = Sessiones.objects.filter(reservacion_id=reservacion)
            sessiones_by_reservacion = [{
                "id": session.id,
                "fecha_inicio": self.format_date(session.fecha_inicio) if session.fecha_inicio else "Sin Iniciar",
                "fecha_fin": self.format_date(session.fecha_fin) if session.fecha_fin else "Sin Terminar",
                "duracion": session.duracion if session.duracion else "Sin Iniciar",
                "is_active": "Valida" if session.is_active else "Invalida",
                "reservacion_id": session.reservacion_id,
                "practica": reservacion.practica_id.titulo
            } for session in sessiones]

            sessions_list = sessions_list + list(sessiones_by_reservacion)
            
        print("")
        print(sessions_list)


        return render(request, self.template_name, {
            "grupo": grupo,
            "alumno": alumno,
            "reservaciones": reservaciones_list,
            "sessiones":sessions_list 
        })

    def post(self, request, *args, **kwargs):
        pass

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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from sessiones.models import Sessiones
from usuarios.models import Usuarios
from utilities import format_date

class AlumnoDetallesSession(LoginRequiredMixin, View):
    login_url = "login/"
    template_name = "AlumnoDetallesSession.html"

    def get(self, request, *args, **kwargs):

        try:
            session_data = Sessiones.objects.get(pk=self.kwargs["session_id"])
            session = {
                "id": session_data.id,
                "fecha_inicio": format_date(session_data.fecha_inicio) if session_data.fecha_inicio else None,
                "fecha_fin": format_date(session_data.fecha_fin) if session_data.fecha_fin else None,
                "duracion": session_data.duracion,
                "is_active": session_data.is_active,
                "session_estatus": "Valida" if session_data.is_active else "Invalida",
                "reservacion_id": session_data.reservacion_id,
            }
            alumno = Usuarios.objects.get(pk=self.kwargs["alumno_id"])

        except Sessiones.DoesNotExist as error:
            print(error)
            return render(request, self.template_name)

        except Usuarios.DoesNotExist as error:
            print(error)
            return render(request, self.template_name)

        return render(request, self.template_name, {
            "grupo_id": self.kwargs["grupo_id"],
            "alumno": alumno,
            "session": session
        })
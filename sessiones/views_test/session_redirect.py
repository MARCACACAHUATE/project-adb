from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from sessiones.models import Reservaciones
from practicas.models import Practicas


class SessionRedirectView(LoginRequiredMixin, View):
    template_name = "SessionRedirect.html"

    def get(self, request, *args, **kwargs):
        try:
            practica_activa = Practicas.objects.get(pk=request.session["practica_activa"])
            reservacion = Reservaciones.objects.get(practica_id=practica_activa)

        except Reservaciones.DoesNotExist:
            messages.info(request, "No tiene una reservacion para esta práctica.")
            return redirect("home")

        return render(request, self.template_name, { 
            "reservacion": reservacion
        })
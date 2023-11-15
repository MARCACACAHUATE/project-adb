from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from practicas.models import Practicas
from practicas.forms import EditPracticaForm

class EditarPracticaView(LoginRequiredMixin, View):
    login_url = "login/"
    template_name = "EditPractica.html"
    form_class = EditPracticaForm

    def get(self, request, *args, **kwargs):
        practica = Practicas.objects.get(pk=self.kwargs["practica_id"])
        practica_data = {
            "id": practica.id,
            "titulo": practica.titulo,
            "descripcion": practica.descripcion,
            "is_valid": practica.is_valid,
            "fecha_inicio": practica.fecha_inicio.strftime("%Y-%m-%dT%H:%M"),
            "fecha_fin": practica.fecha_fin.strftime("%Y-%m-%dT%H:%M")
        }

        return render(request, self.template_name, { 
            "practica_id": self.kwargs["practica_id"],
            "practica": practica_data,
            "grupo_id": self.kwargs["grupo_id"]
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        practica_id = self.kwargs["practica_id"]
        grupo_id = self.kwargs["grupo_id"]

        print(form.is_valid())
        if form.is_valid():
            data = form.cleaned_data

            # Validar que no exista una practica ya creada para esa semana
            practicas_creadas = Practicas.objects.filter(
                fecha_inicio__gte=data["fecha_inicio"],
                fecha_fin__lte=data["fecha_fin"]
            ).count()

            if practicas_creadas > 0:
                message = "Una práctica ya ha sido creada esta semana."      
                print(message)
                print("hola")
                return render(request, self.template_name, { 
                    "practica_id": practica_id,
                    "grupo_id": grupo_id,
                    "error_message": message
                })

            try:
                practica = Practicas.objects.get(pk=practica_id)
                practica.titulo = data["titulo"]
                practica.descripcion = data["descripcion"]
                practica.fecha_inicio = data["fecha_inicio"]
                practica.fecha_fin = data["fecha_fin"]

                #if data["is_valid"] == "True":
                #    practica.is_valid = True

                #elif data["is_valid"] == "False":
                #    practica.is_valid = False

                practica.save()

                return redirect("practicas:list", grupo_id=self.kwargs["grupo_id"])

            except Practicas.DoesNotExist:
                return render(request, self.template_name, { 
                    "practica_id": practica_id,
                    "grupo_id": grupo_id,
                    "error_message": f"La práctica con el id {practica_id} no existe"
                })

        return render(request, self.template_name, { 
            "practica_id": practica_id,
            "grupo_id": grupo_id,
            "error_message": f"Error en el formulario"
        })
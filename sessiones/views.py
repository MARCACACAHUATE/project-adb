from datetime import datetime
from enum import global_enum_repr
import re
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from requests import session
from .models import Reservaciones
from .forms import ReservacionForm, FechaForm
from practicas.models import Practicas, practicas
from django.utils import timezone
# Create your views here. 

from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from sessiones.models import Sessiones

def inicio(request):
    return HttpResponse("<h1>Hola</h1>")

#-------------------------------------------------------------------------------------------------------------------------

def reservaciones(request):
    #Sólo trae las reservaciones con el id del usuario
    user = request.session.get("user_id")
    reservaciones = Reservaciones.objects.filter(alumno_id= user )

    return render(request, 'index.html', {'reservaciones': reservaciones})

#-------------------------------------------------------------------------------------------------------------------------

def crear(request):
    now = timezone.now()
    try:
        Practicas.objects.all().latest('fecha_inicio')
    except Practicas.DoesNotExist:
        return render(request, 'index.html', { "mensaje": f"No hay prácticas disponibles"})

    if request.method == 'POST':
        form = FechaForm(request.POST)
    
        if form.is_valid():
               
            request.session["fecha"] = form.cleaned_data["fecha"]
            return redirect('sessiones:horario')   

    try:
        #practica = Practicas.objects.get(is_valid=True)   
        practica = Practicas.objects.get(pk=request.session.get("practica_activa"))   
        return render(request, 'AlumnoAgendar.html', {'practica': practica, 'hoy': now} )
    except Practicas.DoesNotExist:
        return render(request, 'index.html', { "mensaje": f"No hay prácticas disponibles"})

#-------------------------------------------------------------------------------------------------------------------------


def horario(request):
    user = request.session.get("user_id")
    request.session['horas'] = ['00','01','02', '03', '04', '05','06', '07', '09', '10','11', '12', '13', '14','15', '16', '17', '18','19', '20', '21', '22','23']
    #ultima_practica = Practicas.objects.latest('fecha_inicio')
    ultima_practica = Practicas.objects.get(pk=request.session.get("practica_activa"))   

    if request.method == 'POST':
        form = ReservacionForm(request.POST)
    
        if form.is_valid():
    
            try:
                #Valores para validar las reservaciones 
                ultima_reservacion_user = Reservaciones.objects.filter(alumno_id= user).latest('fecha_reservacion')

                #Valida que su última reservación ya haya terminado y que no vuelva a reservar la misma práctica
                if ultima_reservacion_user.fecha_reservacion < ultima_practica.fecha_inicio:
                        fecha = request.session["fecha"] + ' ' + form.cleaned_data["fecha_reservacion"]
                        
                        #Crea la reservación con el id del usuario y la fecha seleccionada 
                        reservacion = Reservaciones(practica_id_id= ultima_practica.pk, alumno_id_id= user, fecha_reservacion= fecha )

                        reservacion.save()
                        print(reservacion)
                        return redirect("sessiones:reservaciones")
                else:
                                print("Ya tienes una reservación creada")
                                reservaciones = Reservaciones.objects.filter(alumno_id= user )
                                return render(request, 'index.html', {'reservaciones': reservaciones, 'mensaje': f"Ya tienes una reservación creada"})  
            except Reservaciones.DoesNotExist:
                #Este proceso es por si es la primera reservación del usuario
                fecha = request.session["fecha"] + ' ' + form.cleaned_data["fecha_reservacion"]
                reservacion = Reservaciones(practica_id_id= ultima_practica.pk, alumno_id_id= user, fecha_reservacion= fecha )
                reservacion.save()
                print(reservacion)
                return redirect("sessiones:reservaciones")  
            
    try:
        reservaciones = Reservaciones.objects.filter(fecha_reservacion__date=request.session["fecha"])

        for reservacion in reservaciones:
            hora = reservacion.fecha_reservacion.hour
            print(hora)
            request.session['horas'].remove(str(hora))

        return render(request, 'AlumnoAgendarHora.html', {'horas': request.session['horas'], "practica": ultima_practica })
    except Reservaciones.DoesNotExist:
          return render(request, 'AlumnoAgendarHora.html', {'horas': request.session['horas']})

#-------------------------------------------------------------------------------------------------------------------------


def modificarCita(request, id):
    request.session["reservacion_id"] = id
    reservacion = Reservaciones.objects.get(pk= id)
    return render(request, 'AlumnoModificarCita.html', {'reservacion': reservacion})

#-------------------------------------------------------------------------------------------------------------------------


def reagendar(request):
    now = timezone.now()
    if request.method == 'POST':
        form = FechaForm(request.POST)
        if form.is_valid():
            request.session["fecha"] = form.cleaned_data["fecha"]
            return redirect('sessiones:reagendarHorario')  
    try: 
        #practica = Practicas.objects.get(is_valid=True)   
        practica = Practicas.objects.get(pk=request.session["practica_activa"])   
        return render(request, 'AlumnoReagendar.html', {'practica': practica, 'hoy': now} )
    except Practicas.DoesNotExist:
        return render(request, 'index.html', { "mensaje": f"No hay prácticas disponibles"})
    


#-------------------------------------------------------------------------------------------------------------------------


def reagendarHorario(request):
    request.session['horas'] = ['00','01','02', '03', '04', '05','06', '07', '09', '10','11', '12', '13', '14','15', '16', '17', '18','19', '20', '21', '22','23']
    id_reservacion = request.session.get("reservacion_id")
    user = request.session.get("user_id")
    reagendar = Reservaciones.objects.get(pk= id_reservacion)
    editar = reagendar.reagendar

    if request.method == 'POST':
                form = ReservacionForm(request.POST)
                
                #Con la variable "editar" valida que es la primera vez que va a reagendar
                if form.is_valid() and editar:
                    try:
                        reservacion = Reservaciones.objects.get(pk= id_reservacion)
                        
                        #Cambia el campo "is_valid" de la práctica antigua para que alguien más la pueda reservar
                        hora = reservacion.fecha_reservacion.hour
                        request.session['horas'].append(str(hora))

                        #Agrega la nueva práctica a la reservación y cambia el campo "reagendar" a False para que no pueda volver a reagendar 
                        fecha = request.session["fecha"] + ' ' + form.cleaned_data["fecha_reservacion"]
                    
                        request.session['horas'].remove(str(form.cleaned_data["fecha_reservacion"]))
                        #Crea la reservación con el id del usuario y la fecha seleccionada 
                        reservacion = Reservaciones.objects.filter(pk= reservacion.pk).update(fecha_reservacion=fecha, reagendar=False)
                        print(reservacion)
                        return redirect("sessiones:reservaciones")
                    
                    except Reservaciones.DoesNotExist:
                        return render(request, 'AlumnoAgendar.html', { "mensaje": f"La reservación no existe"})
                else:
                    reservaciones = Reservaciones.objects.filter(alumno_id= user )
                    return render(request, 'index.html', {'reservaciones': reservaciones, 'mensaje': f"Ya no puedes volver a reagendar"})
            
    reservaciones = Reservaciones.objects.filter(fecha_reservacion__date=request.session["fecha"])

    for reservacion in reservaciones:
        hora = reservacion.fecha_reservacion.hour
        hora_formateada = hora 
        if len(str(hora)) < 2:
            print(f"0{hora}")
            hora_formateada = f"0{hora}"

        request.session['horas'].remove(str(hora_formateada))

    return render(request, "AlumnoModificarHora.html", {'horas': request.session['horas']})


#-------------------------------------------------------------------------------------------------------------------------


def eliminar(request, id):
    reservacion = Reservaciones.objects.get(id=id)
    hora = reservacion.fecha_reservacion.hour
    request.session['horas'].append(str(hora))
    reservacion.delete()
    return redirect("sessiones:reservaciones")



class SessionRedirectView(LoginRequiredMixin, View):
    template_name = "SessionRedirect.html"

    def get(self, request, *args, **kwargs):
        try:
            validacion: bool = True
            message: str = ""
            practica_activa = Practicas.objects.get(pk=request.session["practica_activa"])
            reservacion = Reservaciones.objects.get(practica_id=practica_activa)

            # valicaion reservacion es valida
            if reservacion.is_valid is not True:
                validacion = False
                message = "La reservacion ya no es valida"

            # validacion fecha y hora
            actual = datetime.now()
            if reservacion.fecha_reservacion.day is not actual.day or reservacion.fecha_reservacion.hour is not actual.hour:
                validacion = False
                message = "Aún no es hora para su reservación"

            # verifica que la practica sigue activa
            if practica_activa.is_valid is not True:
                validacion = False
                message = "La práctica ya no esta activa"

            # Crea o trae el registro de sesion
            session, created = Sessiones.objects.get_or_create(
                reservacion_id = reservacion,
                defaults = { "fecha_inicio": datetime.now() }
            )

        except Reservaciones.DoesNotExist:
            messages.info(request, "No tiene una reservacion para esta práctica.")
            return redirect("home")

        return render(request, self.template_name, { 
            "reservacion": reservacion,
            "validacion": validacion,
            "session": session,
            "message": message
        })


class SessionRegisterView(LoginRequiredMixin, View):
    login_url = "login/"
    template_name = "SessionRegister.html"

    # Se muestra que se tiene que iniciar o terminar la sesion
    # Al iniciar la sesion (ingresar a esta vista), se creara el registro de la sesion
    # Al marcar como termianda se actualizara la fecha de fin
    # y hara el calculo de la duracion de la sesion.
    def get(self, request, *args, **kwargs):
        try:
            session = Sessiones.objects.get(pk=self.kwargs["session_id"])

            if(session.is_active):
                estado = "Activa"
            else:
                estado = "Finalizada"

            session_data = {
                "id": session.id,
                "fecha_inicio": session.fecha_inicio,
                "fecha_fin": session.fecha_fin,
                "duracion": session.duracion,
                "is_active": estado,
                "reservacion_id": session.reservacion_id
            }

        except Sessiones.DoesNotExist:
            print(f"Session con id {self.kwargs['session_id']} no existe")

        return render(request, self.template_name, {
            "session": session_data
        })

    def post(self, request, *args, **kwargs):

        try:
            session = Sessiones.objects.get(pk=self.kwargs["session_id"])
            session.fecha_fin = datetime.now()

            diff_time = session.fecha_fin - session.fecha_inicio
            print(diff_time)
            hora = diff_time.seconds // 3600
            minutos = (diff_time.seconds % 3600) // 60
            session.duracion = self.format_diff_time(str(hora), str(minutos))
            session.is_active = False

            session.save()

        except Sessiones.DoesNotExist:
            print(f"Session con id {self.kwargs['session_id']} no existe")

        return redirect("sessiones:session_register", session_id=session.id)
    
    def format_diff_time(self, hora: str, minutos: str) -> str:
        if len(hora) < 2:
            hora_formateada = f"0{hora}"
        else:
            hora_formateada = f"{hora}"

        if len(minutos) < 2:
            minutos_formateada = f"0{minutos}"
        else:
            minutos_formateada = f"{minutos}"
        
        return f"{hora_formateada}:{minutos_formateada}"
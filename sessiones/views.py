import datetime
from enum import global_enum_repr
from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests import session
from .models import Reservaciones
from .forms import ReservacionForm, FechaForm
from practicas.models import Practicas, practicas
from django.utils import timezone
# Create your views here. 


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
        practica = Practicas.objects.get(is_valid=True)   
        return render(request, 'AlumnoAgendar.html', {'practica': practica, 'hoy': now} )
    except Practicas.DoesNotExist:
        return render(request, 'index.html', { "mensaje": f"No hay prácticas disponibles"})
    

#-------------------------------------------------------------------------------------------------------------------------


def horario(request):
    user = request.session.get("user_id")
    request.session['horas'] = ['00','01','02', '03', '04', '05','06', '07', '09', '10','11', '12', '13', '14','15', '16', '17', '18','19', '20', '21', '22','23', '24' ]
    ultima_practica = Practicas.objects.latest('fecha_inicio')

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

        return render(request, 'AlumnoAgendarHora.html', {'horas': request.session['horas']})
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
        practica = Practicas.objects.get(is_valid=True)   
        return render(request, 'AlumnoReagendar.html', {'practica': practica, 'hoy': now} )
    except Practicas.DoesNotExist:
        return render(request, 'index.html', { "mensaje": f"No hay prácticas disponibles"})
    


#-------------------------------------------------------------------------------------------------------------------------


def reagendarHorario(request):
    id_reservacion = request.session.get("reservacion_id")
    user = request.session.get("user_id")
    reagendar = Reservaciones.objects.get(pk= id_reservacion)
    editar = reagendar.reagendar
    ultima_practica = Practicas.objects.latest('fecha_inicio')

    if request.method == 'POST':
                form = ReservacionForm(request.POST)
                
                #Con la variable "editar" valida que es la primera vez que va a reagendar
                if form.is_valid() and editar:
                    try:
                        reservacion = Reservaciones.objects.get(pk= id_reservacion)
                        practica_id = reservacion.practica_id_id
                        practica = Practicas.objects.get(pk= practica_id)
                        
                        
                        #Valida que el cambio sea de la misma práctica
                        if practica.titulo == ultima_practica.titulo:

                            #Cambia el campo "is_valid" de la práctica antigua para que alguien más la pueda reservar
                            hora = reservacion.fecha_reservacion.hour
                            request.session['horas'].append(str(hora))

                            #Agrega la nueva práctica a la reservación y cambia el campo "reagendar" a False para que no pueda volver a reagendar 
                            fecha = request.session["fecha"] + ' ' + form.cleaned_data["fecha_reservacion"]
                        
                            request.session['horas'].remove(str(form.cleaned_data["fecha_reservacion"]))
                            #Crea la reservación con el id del usuario y la fecha seleccionada 
                            reservacion = Reservaciones.objects.filter(pk= reservacion.pk).update(fecha_reservacion= fecha, reagendar=False)
                            print(reservacion)
                            return redirect("sessiones:reservaciones")
                        else: 
                            reservaciones = Reservaciones.objects.filter(alumno_id= user )
                            return render(request, 'index.html', {'reservaciones': reservaciones, 'mensaje': f"No puedes reagendar una práctica diferente"})
                            
                    
                    except Reservaciones.DoesNotExist:
                        return render(request, 'AlumnoAgendar.html', { "mensaje": f"La reservación no existe"})
                else:
                    reservaciones = Reservaciones.objects.filter(alumno_id= user )
                    return render(request, 'index.html', {'reservaciones': reservaciones, 'mensaje': f"Ya no puedes volver a reagendar"})
            
    reservaciones = Reservaciones.objects.filter(fecha_reservacion__date=request.session["fecha"])

    for reservacion in reservaciones:
            hora = reservacion.fecha_reservacion.hour
            request.session['horas'].remove(str(hora))

    return render(request, "AlumnoModificarHora.html", {'horas': request.session['horas']})


#-------------------------------------------------------------------------------------------------------------------------


def eliminar(request, id):
    reservacion = Reservaciones.objects.get(id=id)
    hora = reservacion.fecha_reservacion.hour
    request.session['horas'].append(str(hora))
    reservacion.delete()
    return redirect("sessiones:reservaciones")


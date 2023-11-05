from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reservaciones
from .forms import ReservacionForm
from practicas.models import Practicas
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here. 


def inicio(request):
    return HttpResponse("<h1>Hola</h1>")

#-------------------------------------------------------------------------------------------------------------------------

def reservaciones(request):
    #Sólo trae las reservaciones con el id del usuario
    user = request.session.get("user_id")
    reservaciones = Reservaciones.objects.filter(alumno_id= user )
    print(reservaciones)

    return render(request, 'index.html', {'reservaciones': reservaciones})

#-------------------------------------------------------------------------------------------------------------------------

def crear(request):
    user = request.session.get("user_id")

    if request.method == 'POST':
        form = ReservacionForm(request.POST)
    
        if form.is_valid():
    
            try:
                #Valores para validar las reservaciones 
                reservaciones = Reservaciones.objects.filter(alumno_id= user)
                now = timezone.now()
                ultima_reservacion = Reservaciones.objects.filter(alumno_id= user).latest('fecha_reservacion')
                ultima_reservacion_fecha = Practicas.objects.get(pk= ultima_reservacion.practica_id_id)
                practica = Practicas.objects.get(pk=form.cleaned_data["practica_id"])

                #Valida que su última reservación ya haya terminado y que no vuelva a reservar la misma práctica
                if ultima_reservacion_fecha.fecha_fin < now and ultima_reservacion_fecha.titulo != practica.titulo :
                        
                        #Crea la reservación con el id del usuario y la fecha seleccionada 
                        reserva = Reservaciones(practica_id= practica, alumno_id_id= user)

                        #Cambia el campo "is_valid" de la práctica seleccionada para que alguien más no la pueda reservar
                        Practicas.objects.filter(pk=form.cleaned_data["practica_id"]).update(is_valid= False)
                        reserva.save()
                        print(reserva)
                        return redirect("sessiones:reservaciones")
                else:
                                print("Ya tienes una reservación creada")
                                reservaciones = Reservaciones.objects.filter(alumno_id= user )
                                return render(request, 'index.html', {'reservaciones': reservaciones, 'mensaje': f"Ya tienes una reservación creada"})
                
            except Practicas.DoesNotExist:
                    return render(request, 'crearReservacion.html', { "mensaje": f"La práctica con id {form.cleaned_data['practica_id']} no existe"})
            except Reservaciones.DoesNotExist:
                #Este proceso es por si es la primera reservación del usuario

                practica = Practicas.objects.get(pk=form.cleaned_data["practica_id"])
                reserva = Reservaciones(practica_id= practica, alumno_id_id= user)
                Practicas.objects.filter(pk=form.cleaned_data["practica_id"]).update(is_valid= False)
                reserva.save()
                print(reserva)
                return redirect("sessiones:reservaciones")
    
            
    practicas = Practicas.objects.filter(is_valid= True)
    return render(request, 'AlumnoAgendar.html', {'practicas': practicas})

#-------------------------------------------------------------------------------------------------------------------------

def reagendar(request, id):
    user = request.session.get("user_id")
    reagendar = Reservaciones.objects.get(pk=id)
    editar = reagendar.reagendar

    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        
        #Con la variable "editar" valida que es la primera vez que va a reagendar
        if form.is_valid() and editar:
            try:
                reservacion = Reservaciones.objects.get(pk= id)
                practica_id = reservacion.practica_id_id
                practica = Practicas.objects.get(pk=form.cleaned_data["practica_id"])
                practica_titulo = Practicas.objects.get(pk=practica_id)
                
                #Valida que el cambio sea de la misma práctica
                if practica_titulo.titulo == practica.titulo:

                    #Cambia el campo "is_valid" de la práctica antigua para que alguien más la pueda reservar
                    Practicas.objects.filter(pk=practica_id).update(is_valid= True)

                    #Agrega la nueva práctica a la reservación y cambia el campo "reagendar" a False para que no pueda volver a reagendar 
                    Reservaciones.objects.filter(pk= id).update(practica_id= practica, reagendar= False)

                    #Cambia el campo "is_valid" de la práctica seleccionada para que alguien más no la pueda reservar
                    Practicas.objects.filter(pk=form.cleaned_data["practica_id"]).update(is_valid= False)
                    
                    return redirect("sessiones:reservaciones")
                else: 
                      reservaciones = Reservaciones.objects.filter(alumno_id= user )
                      return render(request, 'index.html', {'reservaciones': reservaciones, 'mensaje': f"No puedes reagendar una práctica pasada"})
                     
            
            except Practicas.DoesNotExist:
                return render(request, 'AlumnoAgendar.html', { "mensaje": f"La práctica con id {form.cleaned_data['practica_id']} no existe"})
        else:
            
             reservaciones = Reservaciones.objects.filter(alumno_id= user )
             return render(request, 'index.html', {'reservaciones': reservaciones, 'mensaje': f"Ya no puedes volver a reagendar"})
    
    practicas = Practicas.objects.filter(is_valid= True)
    return render(request, 'AlumnoReagendar.html', {'practicas': practicas})

#-------------------------------------------------------------------------------------------------------------------------

def eliminar(request, id):
    reservacion = Reservaciones.objects.get(id=id)
    reservacion.delete()
    Practicas.objects.filter(id= reservacion.practica_id.id).update(is_valid= True)
    return redirect("sessiones:reservaciones")

def modificarCita(request, id):
     reservacion = Reservaciones.objects.get(pk= id)
     return render(request, 'AlumnoModificarCita.html', {'reservacion': reservacion})
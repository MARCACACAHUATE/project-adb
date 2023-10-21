from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from django.contrib.auth.models import User

from usuarios.forms import UserCreationForm, UserChangeForm
from usuarios.models import Usuarios

def home(request):

    return render(request, "login.html")

#signup
def registro(request):

    form = UserCreationForm()

    if request.method == 'POST':
        
        #password_confirm = request.POST['password_confirm']
        
        if UserChangeForm.is_valid(request):

            usuarios = Usuarios()

            usuarios.role_id = form.cleaned_data['role_id']
            usuarios.nombre = form.cleaned_data['nombre']
            usuarios.matricula = form.cleaned_data['matricula']
            usuarios.correo = form.cleaned_data['correo']
            usuarios.password = form.cleaned_data['password']

        #if password==password_confirm:
         #   if Usuarios.objects.filter(matricula=matricula).exists():
          #      messages.info(request, 'Username is already taken')
           #     return redirect(registro)
            #elif Usuarios.objects.filter(correo=correo).exists():
             #   messages.info(request, 'Email is already taken')
              #  return redirect(registro)

        
        #user = Usuarios.objects.create_user(role_id=role_id, matricula=matricula, password=password, correo=correo, nombre=nombre)
            usuarios.save()
                
        else:
            print("Invalido")

    
    return render(request, 'registro.html')



    
#, {
        #"form": UserCreationForm
        #})
    


def alumnoinicio(request):

    return render(request, "AlumnoInicio.html")


def maestroinicio(request):

    return render(request, "MaestroMenu.html")





# Create your views here.

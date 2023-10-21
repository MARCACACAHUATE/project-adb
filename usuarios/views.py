from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from django.contrib.auth.models import User

from usuarios.forms.registrouser import CustomUserForm
from django.contrib.auth import login, authenticate

from usuarios.models import Usuarios

def home(request):

    return render(request, "login.html")

#signup
def registro(request):    
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()   
            role_id = formulario.cleaned_data['role_id']
            nombre = formulario.cleaned_data['nombre']
            matricula = formulario.cleaned_data['matricula']
            correo = formulario.cleaned_data['correo']
            password = formulario.cleaned_data['password']        
            return render(request, 'login.html', {"form": formulario, "mensaje": 'ok'})

    return render(request, 'registro.html')


def alumnoinicio(request):

    return render(request, "AlumnoInicio.html")


def maestroinicio(request):

    return render(request, "MaestroMenu.html")





# Create your views here.

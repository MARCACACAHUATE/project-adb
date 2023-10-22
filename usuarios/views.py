import traceback
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from usuarios.forms.registrouser import CustomUserForm
from usuarios.forms import FormularioRegistro
from django.contrib.auth import login, authenticate

from usuarios.models import Usuarios, Role

def home(request):
    if request.method == 'POST':
        print(request.POST["matricula"])
        matricula = request.POST["matricula"]
        print(request.POST["password"])
        password = request.POST["password"]
        user = authenticate(request, matricula=matricula, password=password)

        if user is not None:
            if user.role_id.Role == "Alumno":
                print("session iniciada")
                return redirect("/alumnoinicio")
            else:
                return redirect("/maestroinicio")
        else:
            print("Credenciales invalidas")

    return render(request, "login.html")


def registro(request):    

    if request.method == 'POST':

        formulario = FormularioRegistro(request.POST)
        print(formulario.is_valid())
        if formulario.is_valid():

            try:

                #alumno = Usuarios.objects.get(matricula=formulario.cleaned_data["matricula"])
                #alumno.is_verified = True

                role_id = formulario.cleaned_data["role_id"]
                role = Role.objects.get(pk=role_id)

                Usuarios.objects.create_user(
                    correo=formulario.cleaned_data['correo'],
                    nombre = formulario.cleaned_data['nombre'],
                    role_id = role,
                    matricula = formulario.cleaned_data['matricula'],
                    password = formulario.cleaned_data['password']
                )

                return redirect("/")

            except Exception as error:
                print(error)
                print(type(error).__name__)
                traceback.print_exc()

        else:
            print("Formulario Invalido")
            return render(request, 'registro.html', {
                "form": formulario,
                "mensaje": 'error en el formulario'
            })

    return render(request, 'registro.html')


def alumnoinicio(request):

    return render(request, "AlumnoInicio.html")


def maestroinicio(request):

    return render(request, "MaestroMenu.html")





# Create your views here.

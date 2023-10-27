import traceback
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from usuarios.forms.registrouser import CustomUserForm
from usuarios.forms import FormularioRegistro
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from usuarios.models import Usuarios, Role

def login_user(request):

    if request.method == 'POST':
        matricula = request.POST["matricula"]
        password = request.POST["password"]
        user = authenticate(request, matricula=matricula, password=password)

        if user is not None:
                request.session["role"] = user.role_id.Role
                login(request, user)
                return redirect("/")
        else:
            print("Credenciales invalidas")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("/login/")


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


@login_required(login_url="login/")
def home(request):
    print()
    if request.session["role"] == "Alumno":
        return render(request, "AlumnoInicio.html")

    if request.session["role"] == "Maestro":
        return render(request, "MaestroMenu.html")

    return render(request, "AdminInicio.html")


def registromaestros(request):
    maestro_id = Role.objects.get(Role="Maestro")

    if request.method == 'POST':

        formulario = FormularioRegistro(request.POST)
        print(formulario.is_valid())
        if formulario.is_valid():

            try:

                role_id = formulario.cleaned_data["role_id"]
                role = Role.objects.get(pk=role_id)

                Usuarios.objects.create_user(
                    matricula = formulario.cleaned_data['matricula'],
                    password = formulario.cleaned_data['password'],
                    is_maestro=True,
                    correo=formulario.cleaned_data['correo'],
                    nombre = formulario.cleaned_data['nombre'],
                    role_id = role,
                )

                return render(request, "AdminInicio.html")

            except Exception as error:
                print(error)
                print(type(error).__name__)
                traceback.print_exc()

        else:
            print("Formulario Invalido")
            return render(request, 'RegistroMaestros.html', {
                "form": formulario,
                "mensaje": 'error en el formulario'
            })

    return render(request, "RegistroMaestros.html", { "maestro_id": maestro_id.id })
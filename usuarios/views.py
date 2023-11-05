import traceback
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from usuarios.forms.registrouser import CustomUserForm
from usuarios.forms import FormularioRegistro
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from usuarios.models import Usuarios, Role, Registro_Semestre

def login_user(request):

    if request.method == 'POST':
        matricula = request.POST["matricula"]
        password = request.POST["password"]
        user = authenticate(request, matricula=matricula, password=password)

        if user is not None:
                request.session["role"] = user.role_id.Role
                request.session["user_id"] = user.id

                login(request, user)
                return redirect("/")
        else:
            return render(request, "login.html", {
                "mensaje": "Credenciales invalidas"
            })

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("/login/")


def registro(request):    

    if request.method == 'POST':

        formulario = FormularioRegistro(request.POST)

        if formulario.is_valid():

            try:

                alumno = Usuarios.objects.get(matricula=formulario.cleaned_data["matricula"])
                registro_semestre = Registro_Semestre.objects.get(alumno_id=alumno)

                alumno.is_verified = True
                registro_semestre.is_valid = True

                alumno.correo= formulario.cleaned_data['correo']
                alumno.nombre = formulario.cleaned_data['nombre']
                alumno.set_password(formulario.cleaned_data['password'])
                alumno.save()

                return redirect("/")

            except Exception as error:
                print(error)
                print(type(error).__name__)
                traceback.print_exc()
                return render(request, 'registro.html', {
                    "form": formulario,
                    "mensaje": 'El estudiante no tiene un pre registro previo'
                })

        else:
            print("Formulario Invalido")
            return render(request, 'registro.html', {
                "form": formulario,
                "mensaje": 'Error en los datos del formulario'
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


def perfil(request):
    usuario = request.user

    if request.session["role"] == "Alumno":
        return render(request, "Perfil.html", {'usuario': usuario})
    
    if request.session["role"] == "Maestro":
        return render(request, "PerfilMaestro.html", {'usuario': usuario})    
    
    if request.session["role"] == "Admin":
        return render(request, "PerfilAdmin.html", {'usuario': usuario})
    
    return redirect("home")



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
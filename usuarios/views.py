import traceback
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from django.views import View
from usuarios.forms.registrouser import CustomUserForm
from usuarios.forms import FormularioRegistro
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from usuarios.models import Usuarios, Role, Registro_Semestre
from grupos.models import Grupos
from practicas.models import Practicas

from usuarios.forms.passwordchangeform import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash

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


def validar_dominio_correo(correo):
    # Validar que el dominio sea "example.com"
    dominio_permitido = "uanl.edu.mx"
    _, dominio = correo.split('@')
    return dominio == dominio_permitido


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

                if not validar_dominio_correo(alumno.correo):
                    return render(request, 'registro.html', {
                    "form": formulario,
                    "mensaje": 'El dominio del correo electrónico no es válido. Favor de ingresar el dominio @uanl.edu.mx'
                })
                    

                alumno.save()

                return redirect("/")

            except Exception as error:
                print(error)
                print(type(error).__name__)
                traceback.print_exc()
                return render(request, 'registro.html', {
                    "form": formulario,
                    "mensaje": 'El estudiante no tiene un registro previo'
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

    if request.session["role"] == "Alumno":
        alumno = Usuarios.objects.get(pk=request.session.get("user_id"))
        grupo_default = Grupos.objects.filter(alumnos=alumno)[0]

        list_practicas = Practicas.objects.filter(grupo_id=grupo_default)

        grupo_data = {
            "numero_brigada": grupo_default.numero_brigada,
            "nombre_maestro": grupo_default.maestro_id.nombre,
        }
        today = datetime.now()

        practica = Practicas.objects.filter(
            fecha_inicio__lte=today,
            fecha_fin__gte=today
        )[0]

        practica_activa = {
            "id": practica.id, 
            "titulo": practica.titulo
        }

        request.session["practica_activa"] = practica.id

        return render(request, "AlumnoInicio.html", {
            "grupo_data": grupo_data,
            "list_practicas": list_practicas,
            "practica_activa": practica_activa,
        })

    if request.session["role"] == "Maestro":
        return render(request, "MaestroMenu.html")

    if request.session["role"] == "Admin":
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

def cambiopassword(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important for maintaining the user's session
            messages.success(request, 'Tu contraseña se actualizo satisfactoriamente!')
            print("Formulario valido")
            return redirect('CambioContraseña')
        else:
            print("Formulario invalido")
            messages.error(request, 'Error en el formulario.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'CambioContrasena.html', {'form': form})


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

                return render(request, "MaestroList.html")

            except Exception as error:
                print(error)
                print(type(error).__name__)
                traceback.print_exc()

        else:
            print("Formulario Invalido")
            return render(request, 'RegistroMaestros.html', {
                "form": formulario,
                "mensaje": 'Algún dato ingresado es incorrecto. Favor de llenar nuevamente los campos.'
            })
    
    return render(request, "RegistroMaestros.html", { "maestro_id": maestro_id.id })



class MaestroListView(View):
    template_name = "MaestroList.html"

    def get(self, request, *args, **kwargs):
        role_maestro = Role.objects.get(Role="Maestro")
        maestro_list = Usuarios.objects.filter(role_id=role_maestro)

        return render(request, self.template_name, { "maestro_list": maestro_list })


class MaestroDetailView(View):
    template_name = "MaestroDetail.html"

    def get(self, request, *args, **kwargs):

        try:
            maestro = Usuarios.objects.get(pk=self.kwargs.get("maestro_id"))
            return render(request, self.template_name, { "maestro": maestro })

        except Usuarios.DoesNotExist:
            return render(request, self.template_name, { "error_message": "hola" })
        


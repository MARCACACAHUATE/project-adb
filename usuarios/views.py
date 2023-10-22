from django.shortcuts import render, redirect
from django.http import HttpResponse

from usuarios.forms.registrouser import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate

from usuarios.models import Usuarios

def home(request):

    return render(request, "login.html")

def login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                matricula = cd['matricula'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse['Usuario Autenticado']
                else:
                    return HttpResponse['El usuario no esta activo']
            else:
                return HttpResponse['La informacion no es correcta']
        
    else:
        form = LoginForm()
        return render (request, 'login.html', {'form': form})

#signup
def registro(request):    

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                           'registro_done.html', 
                             {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 
                      'registro.html',
                        {'user_form': user_form})

    return render(request, 'registro.html')


def alumnoinicio(request):

    return render(request, "AlumnoInicio.html")


def maestroinicio(request):

    return render(request, "MaestroMenu.html")





# Create your views here.

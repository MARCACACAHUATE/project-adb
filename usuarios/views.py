from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm

def home(request):

    return render(request, "login.html")

#signup
def registro(request):

    if request.method == 'GET':
        print('enviando formulario')
    else: 
        print(request.POST)
        print('obteniendo datos')

    return render(request, "registro.html", {
        "form": UserCreationForm
        })
    


def alumnoinicio(request):

    return render(request, "AlumnoInicio.html")


def maestroinicio(request):

    return render(request, "MaestroMenu.html")





# Create your views here.

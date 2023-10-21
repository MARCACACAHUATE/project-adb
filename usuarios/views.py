from django.shortcuts import render

#from django.contrib.auth.forms import UserCreationForm

from usuarios.forms import UserCreationForm

def home(request):

    return render(request, "login.html")

#signup
def registro(request):

    if request.method == 'POST':
        

        print(request.POST)
        print('obteniendo datos')

    else: 
        print('enviando formulario')

    return render(request, "registro.html", {
        "form": UserCreationForm
        })
    


def alumnoinicio(request):

    return render(request, "AlumnoInicio.html")


def maestroinicio(request):

    return render(request, "MaestroMenu.html")





# Create your views here.

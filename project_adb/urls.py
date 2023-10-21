"""
URL configuration for project_adb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from usuarios.views import registro
from usuarios import views
#from usuarios.views import FormularioRegistro, FormularioUsuarioView

urlpatterns = [
    path('', views.home, name="Home"),
    #signup
    path('registro', views.registro, name="Registro"),
    
    #path('registro', FormularioUsuarioView.procesar_registro , name="Registro"),
    #path('', VRegistro.as_view(), name="Registro"),

    path('alumnoinicio', views.alumnoinicio, name="AlumnoInicio"),
    path('maestroinicio', views.maestroinicio, name="MaestroInicio"),
    path('admin', admin.site.urls) 
]

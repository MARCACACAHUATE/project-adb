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
from django.urls import path, include

from usuarios import views

urlpatterns = [

    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('registro', views.registro, name="Registro"),
    path("grupos/", include('grupos.urls', namespace="grupos")),
    path('registro', views.registro, name="Registro"),   
    path('perfil/', views.perfil, name="Perfil"),
    path('registromaestros', views.registromaestros, name="RegistroMaestros"),
    path('admin', admin.site.urls),
    path('sessiones/', include('sessiones.urls', namespace="sessiones")),
    path("maestros/", views.MaestroListView.as_view(), name="maestros_list"),
    path("maestros/<int:maestro_id>", views.MaestroDetailView.as_view(), name="maestros_detail"),
    # develop urls
    path("__reload__/", include("django_browser_reload.urls")),
]

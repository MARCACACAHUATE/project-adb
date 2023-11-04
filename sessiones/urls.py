from django.urls import path
from . import views

app_name = "sessiones"

urlpatterns = [
    path('', views.inicio),
    path('reservaciones', views.reservaciones, name='reservaciones'),
    path('reservaciones/crear/', views.crear, name='crear'),
    path('reservaciones/reagendar/<int:id>', views.reagendar, name='reagendar'),
    path('reservaciones/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('reservaciones/editar<int:id>', views.modificarCita, name='editar')
]
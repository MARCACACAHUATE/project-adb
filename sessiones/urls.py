from django.urls import path
from . import views

app_name = "sessiones"

urlpatterns = [
    path('', views.SessionRedirectView.as_view(), name="session_redirect"),
    path('<int:session_id>', views.SessionRegisterView.as_view(), name="session_register"),
    path('reservaciones', views.reservaciones, name='reservaciones'),
    path('reservaciones/crear/', views.crear, name='crear'),
    path('reservaciones/crear/horario', views.horario, name='horario'),
    path('reservaciones/reagendar', views.reagendar, name='reagendar'),
    path('reservaciones/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('reservaciones/editar<int:id>', views.modificarCita, name='editar'),
    path('reservaciones/editar/horario', views.reagendarHorario, name= 'reagendarHorario')
]
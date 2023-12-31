from django.urls import path

from grupos.views import (
    CreateBrigadaView, 
    CreateGrupoView, 
    ListGruposView, 
    GruposListRegisterView,
    DeactivateGrupoView,
    ActivateGrupoView,
    DetallesAlumnoGrupoView,
    AlumnoDetallesSession
) 
from practicas.views import CreatePracticasView, UploadActView, activate_practicas, ListaPracticasView

app_name = 'grupos'  # Esto define un espacio de nombres para las URLs de la aplicación

urlpatterns = [
    path('', CreateBrigadaView.as_view(), name='home'),
    path("<int:grupo_id>", CreateBrigadaView.as_view(), name="detail"),
    path("<int:grupo_id>/estudiante/<int:alumno_id>", DetallesAlumnoGrupoView.as_view(), name="alumno_detalles"),
    path("<int:grupo_id>/estudiante/<int:alumno_id>/sessions/<int:session_id>", AlumnoDetallesSession.as_view(), name="alumno_sessiones"),
    #path("<int:grupo_id>/estudiante/<int:alumno_id>/reservacion/<int:reservacion_id>", .as_view(), name="alumno_reservacion"),
    path('create', CreateGrupoView.as_view(), name="create_grupo"),
    #path('list', ListGruposView.as_view(), name="list"),
    path('list', GruposListRegisterView.as_view(), name="list"),
    path('<int:grupo_id>/deactivate', DeactivateGrupoView.as_view(), name='deactivate'),
    path('<int:grupo_id>/activate', ActivateGrupoView.as_view(), name='activate'),
]
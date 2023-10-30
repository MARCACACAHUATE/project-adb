from django.urls import path
from grupos.views import CreateBrigadaView, CreateGrupoView, ListGruposView
from practicas.views import CreatePracticasView

app_name = 'grupos'  # Esto define un espacio de nombres para las URLs de la aplicación

urlpatterns = [
    path('', CreateBrigadaView.as_view(), name='home'),
    path("<int:grupo_id>", CreateBrigadaView.as_view(), name="detail"),
    path('create', CreateGrupoView.as_view(), name="create_grupo"),
    path('list', ListGruposView.as_view(), name="list"),
    path('crear_practicas/', CreatePracticasView.as_view(), name='crear_practicas')
]
from django.urls import path
from grupos.views import CreateBrigadaView, CreateGrupoView

app_name = 'grupos'  # Esto define un espacio de nombres para las URLs de la aplicación

urlpatterns = [
    path('', CreateBrigadaView.as_view(), name='home'),
    path('create', CreateGrupoView.as_view(), name="create_grupo"),
]
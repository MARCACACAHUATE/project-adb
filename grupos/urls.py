from django.urls import path
from grupos.views import CreateBrigadaView, CreateGrupoView, ListGruposView, GruposListRegisterView
from practicas.views import CreatePracticasView, UploadActView, activate_practicas



app_name = 'grupos'  # Esto define un espacio de nombres para las URLs de la aplicación

urlpatterns = [
    path('', CreateBrigadaView.as_view(), name='home'),
    path("<int:grupo_id>", CreateBrigadaView.as_view(), name="detail"),
    path('create', CreateGrupoView.as_view(), name="create_grupo"),
    #path('list', ListGruposView.as_view(), name="list"),
    path('list', GruposListRegisterView.as_view(), name="list"),
    path('crear_practicas/', CreatePracticasView.as_view(), name='crear_practicas'),
    path('subir_practicas/', UploadActView.as_view(), name='upload_Act'),

    path('maestrospracticas/', activate_practicas.maestropracticas, name="MaestroPracticas"),

]
from django.urls import path

from practicas.views import (
    CreatePracticasView, 
    UploadActView, 
    activate_practicas, 
    ListaPracticasView
)

app_name = 'practicas'

urlpatterns = [
    path('grupo/<int:grupo_id>', CreatePracticasView.as_view(), name='crear'),
    path("grupo/<int:grupo_id>/list", ListaPracticasView.as_view(), name="list"),
    # no las he revisado
    path('subir_practicas/', UploadActView.as_view(), name='upload_Act'),
    path('ver/', UploadActView.as_view(), name='upload_Act'),
    path('maestrospracticas/', activate_practicas.maestropracticas, name="MaestroPracticas"),
]
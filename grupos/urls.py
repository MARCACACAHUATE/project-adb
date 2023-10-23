from django.urls import path
from grupos.views import CreateBrigadaView

app_name = 'grupos'  # Esto define un espacio de nombres para las URLs de la aplicación

urlpatterns = [
    path('', CreateBrigadaView.as_view(), name='index'),
    #path('detalle/<int:id>/', views.detalle, name='detalle'),
]
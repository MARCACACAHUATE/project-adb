from django.urls import path
from usuarios.views import MaestroListView

app_name = 'usuarios'

urlpatterns = [
    path("maestros", MaestroListView.as_view(), name="maestros_list"),
]
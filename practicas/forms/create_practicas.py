from django import forms

from usuarios.models import Usuarios 


class CreatePracticasForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    fecha_inicio = forms.DateTimeField()
    fecha_fin = forms.DateTimeField()
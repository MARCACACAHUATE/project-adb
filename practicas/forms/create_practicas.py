from django import forms
from usuarios.models.usuarios import Usuarios 
from grupos.models.grupos import Grupos 
from usuarios.models.usuarios import Usuarios

class CreatePracticasForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    fecha_inicio = forms.DateTimeField()
    fecha_fin = forms.DateTimeField()
    is_valid = forms.BooleanField(initial=True)
    archivo = forms.CharField(max_length=250, required=False)

    grupo_id = forms.ModelChoiceField(queryset=Grupos.objects.all(), required=False)
 
    maestro_id = forms.ModelChoiceField(queryset=Usuarios.objects.all(), required=False)

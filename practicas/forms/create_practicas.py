from django import forms

from grupos.models import Grupos 

class CreatePracticasForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    fecha_inicio = forms.DateTimeField()
    fecha_fin = forms.DateTimeField()
    is_valid = forms.BooleanField(initial=True)
    archivo = forms.CharField(max_length=250, required=False)
    grupo_id = forms.ModelChoiceField(queryset=Grupos.objects.all(), empty_label=None)
    maestro_id = forms.ModelChoiceField(queryset=Grupos.objects.all(), empty_label=None)

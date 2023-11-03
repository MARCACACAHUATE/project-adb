from django import forms

from usuarios.models import Usuarios 


class CreatePracticasForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    fecha_inicio = forms.DateTimeField()
    fecha_fin = forms.DateTimeField()
    is_valid = forms.BooleanField(initial=True, widget=forms.CheckboxInput)
    archivo = forms.CharField(max_length=250, required=False)
    #grupo_id = forms.ModelChoiceField(queryset=Grupos.objects.all(), empty_label="hola")
    grupo_id = forms.IntegerField()
    maestro_id = forms.ModelChoiceField(queryset=Usuarios.objects.all(), empty_label=None)

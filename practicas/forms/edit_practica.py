from datetime import datetime
from django import forms
#from django.utils import timezone
from pytz import timezone

class EditPracticaForm(forms.Form):
    OPCIONES = (
        (True, 'Activa Práctica'),
        (False, 'Desactiva Práctica'),
    )

    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    fecha_inicio = forms.DateTimeField()
    fecha_fin = forms.DateTimeField()
    #is_valid = forms.ChoiceField(
    #    choices=OPCIONES,
    #    widget=forms.Select(attrs={'class': 'tu-clase-css'}),
    #)

    def clean_fecha_inicio(self):
        fecha_inicio: datetime = self.cleaned_data["fecha_inicio"]
        #zona_horaria = timezone('America/Mexico_City')
        #return fecha_inicio.replace(tzinfo=zona_horaria) 
        return fecha_inicio
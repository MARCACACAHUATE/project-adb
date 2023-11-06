from django import forms
from usuarios.models import Usuarios 
from practicas.models import Practicas

#class UploadAct(forms.Form):
 #   actividad_file = forms.FileField()

class UploadActForm(forms.Form):
   #fecha_entrega = forms.DateTimeField()
   #alumno_id = forms.ModelChoiceField(queryset=Usuarios.objects.all(), empty_label=None)
   practica_id = forms.ModelChoiceField(queryset=Practicas.objects.all(), empty_label=None)
   #archivo = forms.CharField(max_length=250)
   archivo = forms.FileField()
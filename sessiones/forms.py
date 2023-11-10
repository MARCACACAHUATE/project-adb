#from django.forms import forms
import datetime
from django import forms

class ReservacionForm(forms.Form):
    fecha_reservacion = forms.CharField()

class FechaForm(forms.Form):
    fecha = forms.CharField()
    
   
#from django.forms import forms
import datetime
from django import forms

class ReservacionForm(forms.Form):
    practica_id = forms.IntegerField()

class FechaForm(forms.Form):
    fecha = forms.CharField()
    
   
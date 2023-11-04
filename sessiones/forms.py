#from django.forms import forms
from django import forms

class ReservacionForm(forms.Form):
    practica_id = forms.IntegerField()
    
   
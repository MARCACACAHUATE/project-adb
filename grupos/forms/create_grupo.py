from django import forms

class CreateGrupoForm(forms.Form):
    numero_brigada = forms.CharField(max_length=10)
    maestro_id = forms.IntegerField()
from django import forms

class UploadAct(forms.Form):
    actividad_file = forms.FileField()


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from usuarios.models.usuarios import Usuarios

class FormularioRegistro(forms.Form):
    matricula = forms.CharField(max_length=10)
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()
    password = forms.CharField()
    password_confirm = forms.CharField()
    role_id = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Las contraseñas no coinciden")

        return cleaned_data


class CustomUserForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['nombre','matricula','correo','password']
 
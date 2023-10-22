from django import forms
from django.contrib.auth.forms import UserCreationForm

from usuarios.models.usuarios import Usuarios

class FormularioRegistro(forms.ModelForm):
    class Meta: 
        model = Usuarios
        fields = '__all__'


class CustomUserForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['nombre','matricula','correo','password']
 
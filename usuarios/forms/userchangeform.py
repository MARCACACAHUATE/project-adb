from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios.models import Usuarios


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuarios
        fields = ("matricula",)
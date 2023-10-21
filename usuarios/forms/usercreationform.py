from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios.models import Usuarios


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Usuarios
        fields = ("matricula", "role_id")

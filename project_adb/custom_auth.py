from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Q
from django.conf import settings
from django.http.request import HttpRequest

class MatriculaBackend(ModelBackend):

    def authenticate(self, request: HttpRequest, matricula: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        Usuarios = get_user_model()

        try:
            user = Usuarios.objects.get(matricula=matricula) 
            if user.check_password(password):
                return user
        except Usuarios.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        Usuario = get_user_model()
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
      
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect
from grupos.models import Grupos


class DeactivateGrupoView(LoginRequiredMixin, View):
    login_url = "login/"

    def get(self, request, *args, **kwargs):
        try:
            grupo = Grupos.objects.get(pk=self.kwargs["grupo_id"])
            grupo.is_active = False
            grupo.save()

        except Grupos.DoesNotExist:
            print(f"Grupo con id {self.kwargs["grupo_id"]} no existe")
            return redirect('grupos:list')
            
        return redirect('grupos:list')
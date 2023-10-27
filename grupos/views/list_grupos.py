from django.shortcuts import render
from django.views import View

from grupos.models import Grupos

class ListGruposView(View):
    template_name = "PantallaReportePracticas.html"

    def get(self, request, *args, **kwargs):

        if request.session.get("role") == "Maestro":
            lista_grupos = Grupos.objects.filter(
                maestro_id__pk=request.session.get("_auth_user_id")
            )
        else:
            lista_grupos = Grupos.objects.all()

        print(lista_grupos)

        return render(request, self.template_name, { "lista_grupos": lista_grupos })

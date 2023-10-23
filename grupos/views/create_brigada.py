import csv
import io
from django.shortcuts import render
from django.views import View
from grupos.forms import UploadCsvAlumnos


class CreateBrigadaView(View):
    form_class = UploadCsvAlumnos
    template_name = "MaestroAltaBrigada.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, { "form": form })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES["csv_file"]
            csv_file.seek(0)
            reader = csv.DictReader(io.StringIO(csv_file.read().decode('utf-8-sig')))
            print(reader)

            for row in reader:
                print(row["matricula"])
                print(row["nombre"])
    
            return render(request, self.template_name)

        else:
            form = self.form_class()
        
        return render(request, self.template_name)

from django import forms


class UploadCsvAlumnos(forms.Form):
    csv_file = forms.FileField()
from django import forms

class EditPracticaForm(forms.Form):
    OPCIONES = (
        (True, 'Activa Práctica'),
        (False, 'Desactiva Práctica'),
    )

    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    fecha_inicio = forms.DateTimeField()
    fecha_fin = forms.DateTimeField()
    #is_valid = forms.ChoiceField(
    #    choices=OPCIONES,
    #    widget=forms.Select(attrs={'class': 'tu-clase-css'}),
    #)
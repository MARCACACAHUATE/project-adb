from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    matricula = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.Form):
    password = forms.CharField(label='passowrd',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='passowrd_confirm',
                               widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['matricula', 'nombre', 'correo']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            return forms.ValidationError('Las contraseñas no son iguales')
        return cd['password2']

 
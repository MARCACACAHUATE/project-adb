from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Contraseña Actual',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'border border-gray-300 w-10/12 px-3 py-2 mb-4 rounded-md bg-gray-100 sm:w-full', 
                                          'placeholder':'Contraseña Actual',
                                          }),
    )                                          
    new_password1 = forms.CharField(
        label='Contraseña Nueva',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'border border-gray-300 w-10/12 px-3 py-2 mb-4 rounded-md bg-gray-100 sm:w-full', 
                                          'placeholder':'Contraseña Actual',
                                          }),
    )                                        
    new_password2 = forms.CharField(
        label='Confirmar Contraseña Nueva',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'border border-gray-300 w-10/12 px-3 py-2 mb-4 rounded-md bg-gray-100 sm:w-full', 
                                          'placeholder':'Contraseña Actual',
                                          }),                                                                                  
    )
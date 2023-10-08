from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProgramadorForm(forms.Form):
    nombre=forms.CharField()
    pais=forms.CharField()

class LenguajeForm(forms.Form):
    nombre=forms.CharField()
    nombrecorto=forms.CharField()

class InstitutoForm(forms.Form):
    nombre=forms.CharField()
    tipo=forms.CharField()

class UsuarioRegistro(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model=User
        fields=["Username","email","first_name","last_name","password1","password2"]
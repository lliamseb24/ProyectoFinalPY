from django import forms 

class ProgramadorForm(forms.Form):
    nombre=forms.CharField()
    pais=forms.CharField()

class LenguajeForm(forms.Form):
    nombre=forms.CharField()
    nombrecorto=forms.CharField()

class InstitutoForm(forms.Form):
    nombre=forms.CharField()
    tipo=forms.CharField()


from django.urls import path
from AppProyecto.views import *
urlpatterns = [
    path('', inicio,name="Inicio"),
    path("programadores/", programador,name="Programadores"),
    path("lenguajes/", Lenguaje,name="Lenguajes"),
    path("institutos/", instituto,name="Institutos"),
    path("programadorform/", programadorform,name="ProgramadorForm"),
    path("lenguajeform/", lenguajeform,name="LenguajeForm"),
    path("institutoform/", institutoform,name="InstitutoForm"),
    path("buscarprogramador/", busquedaprogramador,name="BusquedaProgramador"),
    path("resultado/", resultadobusqueda,name="ResultadoBusqueda"),


]
from django.urls import path
from AppProyecto.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio,name="Inicio"),
    path("programadores/", programador,name="Programadores"),
    path("lenguajes/", Lenguaje,name="Lenguajes"),
    path("institutos/", instituto,name="Institutos"),
    path("buscarprogramador/", busquedaprogramador,name="BusquedaProgramador"),
    path("resultado/", resultadobusqueda,name="ResultadoBusqueda"),
    path("login/", iniciosesion,name="Login"),  
    path("register/", registro,name="Registro"),
    path("logout/", LogoutView.as_view(template_name="AppProyecto/logout.html"),name="Logout"),


    #CRUD Programadores
    path("programadorform/", programadorform,name="ProgramadorForm"),
    path("leerprogramadores/",leerprogramadores,name="ProgramadoresLeer"),
    path("eliminarprogramadores/<prograNombre>/",eliminarprogramadores,name="EliminarProgramador"),
    path("editarprogramadores/<prograNombre>/",editarprogramadores,name="EditarProgramador"),

    #CRUD Institutos
    path("institutoform/", institutoform,name="InstitutoForm"),
    path("leerinstitutos/",leerinstitutos,name="InstitutosLeer"),
    path("eliminarinstitutos/<instiNombre>/",eliminarinstitutos,name="EliminarInstitutos"),

    #CRUD Lenguajes
    path("lenguajeform/", lenguajeform,name="LenguajeForm"),
    path("leerlenguajes/",leerlenguajes,name="LenguajesLeer"),
     path("eliminarlenguajes/<lenguNombre>/",eliminarlenguajes,name="EliminarLenguajes"),


]
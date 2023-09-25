from django.shortcuts import render
from django.http import HttpResponse
from AppProyecto.models import *
from AppProyecto.forms import *

def inicio(request):
    return render(request,"AppProyecto/inicio.html")
     

def programador(request):
    return render(request,"AppProyecto/programadores.html")

    return HttpResponse (f"El usuario creado es: {prog1.nombre} del pais {prog1.pais}")

def Lenguaje(request):
    return render(request,"AppProyecto/lenguajes.html")

def instituto(request):
    return render(request,"AppProyecto/institutos.html")

def programadorform(request):

    if request.method=="POST":
        formulario1=ProgramadorForm(request.POST)
        if formulario1.is_valid():
            info=formulario1.cleaned_data
            programador=Programador(nombre=info["nombre"],pais=info["pais"])
            programador.save()
        return render (request, "AppProyecto/inicio.html")
    
    else:
        formulario1=ProgramadorForm()
    return render (request, "AppProyecto/programadorform.html",{"form1":formulario1})

def lenguajeform(request):

    if request.method=="POST":
        formulario2=LenguajeForm(request.POST)
        if formulario2.is_valid():
            info=formulario2.cleaned_data
            Lenguaje=lenguaje(nombre=info["nombre"],nombrecorto=info["nombrecorto"])
            Lenguaje.save()
        return render (request, "AppProyecto/inicio.html")
    
    else:
        formulario2=LenguajeForm()
    return render (request, "AppProyecto/lenguajeform.html",{"form2":formulario2})

def institutoform(request):

    if request.method=="POST":
        formulario3=InstitutoForm(request.POST)
        if formulario3.is_valid():
            info=formulario3.cleaned_data
            instituto=Instituto(nombre=info["nombre"],tipo=info["tipo"])
            instituto.save()
        return render (request, "AppProyecto/inicio.html")
    
    else:
        formulario3=InstitutoForm()
    return render (request, "AppProyecto/institutoform.html",{"form3":formulario3})


def busquedaprogramador(request):
    return render (request, "AppProyecto/busquedaprogramador.html")

def resultadobusqueda(request):
    return HttpResponse (f"Estas buscando al programador: {request.GET['nombre']}")
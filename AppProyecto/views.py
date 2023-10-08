from django.shortcuts import render
from django.http import HttpResponse
from AppProyecto.models import *
from AppProyecto.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login


def iniciosesion(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario=form.clean_data.get("username")
            contra=form.cleaned_data.get("password")

            user = authenticate(username=usuario,password=contra)

            if user:
                login (request, user)

                return render(request,"AppProyecto/inicio.html",{"Mensaje":f"Bienvenido{user}"})
            else:
                return render(request,"AppProyecto/inicio.html",{"Mensaje":"Datos Incorrectos"})
            
        else:
            form = AuthenticationForm()

        return render(request, "AppProyecto/login.html", {"formulario":form})
    


def registro(request):
    if request.method=="POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username=form.cleaned_data["username"]
            form.save()
            return render (request, "AppProyecto/inicio.html",{"Mensaje":"Usuario Creado"})

        else:
            form = UsuarioRegistro()

            return render (request, "AppProyecto/registro.html",{"formulario":form})


def inicio(request):
    return render(request,"AppProyecto/inicio.html")
     

def programador(request):
    return render(request,"AppProyecto/programadores.html")

    return HttpResponse (f"El usuario creado es: {prog1.nombre} del pais {prog1.pais}")

def Lenguaje(request):
    return render(request,"AppProyecto/lenguajes.html")

def instituto(request):
    return render(request,"AppProyecto/institutos.html")


def busquedaprogramador(request):
    return render (request, "AppProyecto/busquedaprogramador.html")

def resultadobusqueda(request):
    return HttpResponse (f"Estas buscando al programador: {request.GET['nombre']}")


#CRUD PROGRAMADORES

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

def leerprogramadores(request):

    programadores = Programador.objects.all()

    contexto = {"programmers":programadores}
    
    return render (request, "AppProyecto/leerprogramadores.html",contexto)

def eliminarprogramadores (request,prograNombre):
    programador=Programador.objects.get(nombre=prograNombre)        
    programador.delete()

    programadores=Programador.object.all()

    contexto={"programmers":programadores}

    return render(request, "AppProyecto/leerprogramadores.html",contexto)

def editarprogramadores (request, prograNombre):
    programador=Programador.objects.get(nombre=prograNombre)
    if request.method=="POST":
        formulario1=ProgramadorForm(request.POST)
        if formulario1.is_valid():
            info=formulario1.cleaned_data
            programador.nombre =info["nombre"]
            programador.pais =info["pais"]
            programador.save()
        return render (request, "AppProyecto/inicio.html")
    
    else:
        formulario1=ProgramadorForm(initial={"nombre":programador.nombre,"pais":programador.pais})
    return render (request, "AppProyecto/editarprogramador.html",{"form1":formulario1, nombre:"prograNombre"})


#CRUD INSTITUTOS

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

def leerinstitutos(request):

    instituto = Instituto.objects.all()

    contexto = {"institutes":instituto}
    
    return render (request, "AppProyecto/leerinstitutos.html",contexto)

def eliminarinstitutos (request,instiNombre):
    instituto=Instituto.objects.get(nombre=instiNombre)        
    instituto.delete()

    instituto=Instituto.object.all()

    contexto={"institutes":instituto}

    return render(request, "AppProyecto/leerinstitutos.html",contexto)

#CRUD LENGUAJES

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

def leerlenguajes(request):

    lenguajes = lenguaje.objects.all()

    contexto = {"languages":lenguajes}
    
    return render (request, "AppProyecto/leerlenguajes.html",contexto)

def eliminarlenguajes (request,lenguNombre):
    lenguajes=lenguaje.objects.get(nombre=lenguNombre)        
    lenguajes.delete()

    lenguajes=lenguaje.object.all()

    contexto={"languages":lenguajes}

    return render(request, "AppProyecto/leerlenguajes.html",contexto)
from django.db import models

class Programador(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} ---- Pais: {self.pais}"
    
    nombre=models.CharField(max_length=60)
    pais=models.CharField(max_length=30)

class lenguaje(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} ---- Nombre Corto: {self.nombrecorto}"
    
    nombre=models.CharField(max_length=60)
    nombrecorto=models.CharField(max_length=10)

class Instituto(models.Model):
     def __str__(self):
        return f"Nombre: {self.nombre} ---- Tipi: {self.tipo}"
     
nombre=models.CharField(max_length=60)
tipo=models.CharField(max_length=30)
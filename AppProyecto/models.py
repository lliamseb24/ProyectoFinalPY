from django.db import models

class Programador(models.Model):
    nombre=models.CharField(max_length=60)
    pais=models.CharField(max_length=30)

class lenguaje(models.Model):
    nombre=models.CharField(max_length=60)
    nombrecorto=models.CharField(max_length=10)

class Instituto(models.Model):
    nombre=models.CharField(max_length=60)
    tipo=models.CharField(max_length=30)
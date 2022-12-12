from django.db import models
from django.contrib.auth.models import User


class Profesor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email=models.EmailField()
    celular= models.IntegerField()
    edad= models.IntegerField()

    def __str__(self):
        return f' nombre: {self.nombre}, apellido: {self.apellido}'


class Alumno(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    celular= models.IntegerField()
    edad= models.IntegerField()

    def __str__(self):
        return f' nombre: {self.nombre}, apellido: {self.apellido}'



class ClaseGym(models.Model):
    class_name= models.CharField(max_length=50)
    fecha= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f' class_name: {self.class_name}'


class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    imagen= models.ImageField(upload_to='images', null=True, blank=True)






















# Create your models here.

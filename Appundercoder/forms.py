from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CrearProfesorForm(forms.Form):
    nombre= forms.CharField(min_length=5, max_length=40)
    apellido= forms.CharField(max_length=40)
    email=forms.EmailField()
    celular= forms.IntegerField()
    edad= forms.IntegerField()
    
    def __str__(self):
        return f'nombre: {self.nombre},apellido: {self.apellido} - edad: {self.edad}'

class crearAlumnoForm(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    celular= forms.IntegerField()
    edad= forms.IntegerField()

    def __str__(self):
        return f'nombre: {self.nombre},apellido: {self.apellido} - edad: {self.edad}'

class CrearClaseGymForm(forms.Form):
    class_name= forms.CharField(max_length=50)
    fecha= forms.DateTimeField()
    def __str__(self):
        return f'class_name: {self.class_name}'



class registrarForm(UserCreationForm):

    class meta:
        model= User
        fields=[
            "username",
            "email",
            "password1",
            "password2"
        ]

class usereditForm(UserCreationForm):

    class meta:
        model= User
        fields=[
            "username",
            "email",
            "password1",
            "password2"
        ]
        help_text= {k: '' for k in fields}







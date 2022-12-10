from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Appundercoder.forms import CrearProfesorForm, crearAlumnoForm,CrearClaseGymForm,registrarForm,usereditForm
from Appundercoder.models import Profesor, Alumno, ClaseGym
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required








def mostrar_html(request):

    return render(request, "index.html")


def Aboutus(request):
    return render(request, "about.html")

def createprofesor(request):

    if request.method == "POST":
        formulario= CrearProfesorForm(request.POST)

        if formulario.is_valid():
        
            formulario_clean= formulario.cleaned_data

            profesor1= Profesor(nombre= formulario_clean["nombre"], apellido= formulario_clean["apellido"],celular=formulario_clean["celular"], edad= formulario_clean["edad"])

            profesor1.save()

        return render(request, "crearprofe.html")

    else:
        
        formulario= CrearProfesorForm()

    return render(request, "crearprofe.html",{"formulario": CrearProfesorForm})

def createlumnos(request):
    if request.method == "POST":
        formulario= crearAlumnoForm(request.POST)

        if formulario.is_valid():
        
            formulario_clean= formulario.cleaned_data

            alumno1= Alumno(nombre= formulario_clean["nombre"], apellido= formulario_clean["apellido"],celular=formulario_clean["celular"], edad= formulario_clean["edad"])

            alumno1.save()

        return render(request, "crearalumno.html")

    else:
        
        formulario= crearAlumnoForm()

    return render(request, "crearalumno.html",{"formulario": crearAlumnoForm})

def createclass(request):
    if request.method == "POST":
        formulario= CrearClaseGymForm(request.POST)

        if formulario.is_valid():
        
            formulario_clean= formulario.cleaned_data

            clase1= ClaseGym(class_name= formulario_clean["class_name"], fecha= formulario_clean["fecha"])

            clase1.save()

        return render(request, "Crearclase.html")

    else:
        
        formulario= CrearClaseGymForm()

    return render(request, "Crearclase.html",{"formulario": CrearClaseGymForm})

#MOSTRAR PROFESORES#

def mostrarprofesores(request):
   
   profesor = Profesor.objects.all
   
   context = {'profesores': profesor}
   
   return render(request, 'mostrarprofes.html', context=context)

#ELIMINAR PROFESORES#

def eliminar_profesor(request, profesor_id):

        profesor = Profesor.objects.get( id=profesor_id)

        profesor.delete()

        profesor = Profesor.objects.all
   
        context = {'profesores': profesor}
   
        return render(request, 'mostrarprofes.html', context=context)



def actualizar_profesor(request,profesor_id):

        profesor1 = Profesor.objects.get( id = profesor_id)

        if request.method == "POST":

                formulario = CrearProfesorForm(request.POST)
                
                if formulario.is_valid():
                        
                        formulario_limpio = formulario.cleaned_data
                        
                        profesor1.nombre = formulario_limpio["nombre"]
                        profesor1.apellido = formulario_limpio["apellido"]
                        profesor1.email = formulario_limpio["email"]
                        profesor1.celular = formulario_limpio["celular"]
                        profesor1.edad= formulario_limpio["edad"]

                        profesor1.save()
                
                return render(request, "index.html")

        else:
                
                formulario = CrearProfesorForm(initial={"nombre":Profesor.nombre,"apellido":Profesor.apellido,"email":Profesor.email,"celular":Profesor.celular,"edad":Profesor.edad,})

        return render(request, "actualizarprofesor.html", {"formulario" : CrearProfesorForm } )

def buscar_profesor(request):
        
        if request.GET.get("nombre" , False):
                apellido = request.GET["nombre"]
                profesores = Profesor.objects.filter(nombre__icontains=apellido)
                
                return render(request, "buscarprofe.html", {"profesores" : profesores})
        else:
                respuesta = "no hay datos"
        
        return render(request, "buscarprofe.html", {"respuesta" : respuesta} )

def mostraralumnos(request):
   
   alumno = Alumno.objects.all
   
   context = {'alumnos': alumno}
   
   return render(request, 'mostraralumnos.html', context=context)

def eliminar_alumno(request, alumno_id):

        alumno = Alumno.objects.get( id=alumno_id)

        alumno.delete()

        alumno = Alumno.objects.all
   
        context = {'alumnos': alumno}
   
        return render(request, 'mostraralumnos.html', context=context)


def actualizar_alumno(request,alumno_id):

        alumno1 = Alumno.objects.get( id = alumno_id)

        if request.method == "POST":

                formulario = crearAlumnoForm(request.POST)
                
                if formulario.is_valid():
                        
                        formulario_limpio = formulario.cleaned_data
                        
                        alumno1.nombre = formulario_limpio["nombre"]
                        alumno1.apellido = formulario_limpio["apellido"]
                        alumno1.celular = formulario_limpio["celular"]
                        alumno1.edad= formulario_limpio["edad"]

                        alumno1.save()
                
                return render(request, "index.html")

        else:
                
                formulario = crearAlumnoForm(initial={"nombre":Alumno.nombre,"apellido":Alumno.apellido,"celular":Alumno.celular,"edad":Alumno.edad,})

        return render(request, "actualizaralumno.html", {"formulario" : crearAlumnoForm } )

def buscar_alumno(request):
        
        if request.GET.get("nombre" , False):
                apellido = request.GET["nombre"]
                alumnos = Alumno.objects.filter(nombre__icontains=apellido)
                
                return render(request, "buscaralumno.html", {"alumnos" : alumnos})
        else:
                respuesta = "no hay datos"
        
        return render(request, "buscaralumno.html", {"respuesta" : respuesta} )


def mostrarclases(request):
   
   clase = ClaseGym.objects.all
   
   context = {'clases': clase}
   
   return render(request, 'mostrarclases.html', context=context)

def eliminar_clase(request, clase_id):

        clase = ClaseGym.objects.get( id=clase_id)

        clase.delete()

        clase = ClaseGym.objects.all
   
        context = {'clases': clase}
   
        return render(request, 'mostrarclases.html', context=context)


def actualizar_clase(request,clase_id):

        clase1 = ClaseGym.objects.get( id = clase_id)

        if request.method == "POST":

                formulario = CrearClaseGymForm(request.POST)
                
                if formulario.is_valid():
                        
                        formulario_limpio = formulario.cleaned_data
                        
                        clase1.class_name = formulario_limpio["class_name"]
                        clase1.fecha = formulario_limpio["fecha"]

                        clase1.save()
                
                return render(request, "index.html")

        else:
                
                formulario = CrearClaseGymForm(initial={"class_name":ClaseGym.class_name,"fecha":ClaseGym.fecha})

        return render(request, "actualizarclase.html", {"formulario" : CrearClaseGymForm } )

def buscar_clase(request):
        
        if request.GET.get("nombre" , False):
                fecha = request.GET["nombre"]
                clases = ClaseGym.objects.filter(class_name__icontains=fecha)
                
                return render(request, "buscarclase.html", {"clases" : clases})
        else:
                respuesta = "no hay datos"
        
        return render(request, "buscarclase.html", {"respuesta" : respuesta} )


class registrarView(CreateView):

        form_class= registrarForm

        success_url= reverse_lazy('mostrar')

        template_name="register.html"

class iniciarsesionView(LoginView):
        template_name="iniciarsesion.html"


class cerrarsesionView(LogoutView):
        template_name="cerrarsesion.html"

def editaruser(request,):

        usuario1 = request.user

        if request.method == "POST":

                formulario = usereditForm(request.POST)
                
                if formulario.is_valid():
                        
                        formulario_limpio = formulario.cleaned_data
                        
                        usuario1.username = formulario_limpio["username"]
                        usuario1.password1 = formulario_limpio["password1"]
                        usuario1.password2 = formulario_limpio["password2"]


                        usuario1.save()
                
                return render(request, "index.html")

        else:
                formulario_limpio= usereditForm(initial={
                        'username':usuario1.username,
                })

        return render(request, "actualizaruser.html",{
                'formulario':formulario_limpio,
                'usuario': usuario1
        })















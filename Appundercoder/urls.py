"""UnderCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
from .views import Aboutus,createprofesor,createlumnos,createclass,mostrarprofesores,eliminar_profesor,actualizar_profesor,buscar_profesor,mostraralumnos,eliminar_alumno,actualizar_alumno,buscar_alumno,mostrarclases,eliminar_clase,actualizar_clase,buscar_clase,editaruser

urlpatterns = [
    path('', views.mostrar_html, name='mostrar'),
    path('admin/', admin.site.urls),
    path('aboutus/', Aboutus, name='nosotros'),
    path("crearprofesor/",createprofesor,name='crearprofesor'),
    path("crearalumnos/",createlumnos,name='crearalumno' ),
    path("crearclase/", createclass, name='crearclase'),
    path('mostrar_profesores/',mostrarprofesores, name='mostrarprofe'),
    path('eliminarprofesor/<profesor_id>', eliminar_profesor, name='Eliminar Profesor'),
    path('actualizarprofesor/<profesor_id>', actualizar_profesor, name='Actualizar Profesor'),
    path("buscar_profesor/", buscar_profesor, name = "buscar_profesor"),
    path('mostrar_alumnos/',mostraralumnos, name='mostraralumno'),
    path('eliminaralumno/<alumno_id>', eliminar_alumno, name='Eliminar Alumno'),
    path('actualizaralumno/<alumno_id>', actualizar_alumno, name='Actualizar Alumno'),
    path("buscar_alumno/", buscar_alumno, name = "buscar_alumno"),
    path('mostrar_clases/',mostrarclases, name='mostrarclase'),
    path('eliminarclase/<clase_id>', eliminar_clase, name='Eliminar ClaseGym'),
    path('actualizarclase/<clase_id>', actualizar_clase, name='Actualizar ClaseGym'),
    path("buscar_clase/", buscar_clase, name = "buscar_clase"),
    path("registrar/", views.registrarView.as_view() ,name = "registrar"),
    path("iniciarsesion/", views.iniciarsesionView.as_view() ,name = "iniciarsesion"),
    path("cerrarsesion/", views.cerrarsesionView.as_view() ,name = "cerrarsesion"),
    path("editarusuario/", editaruser,name = "editaruser"),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

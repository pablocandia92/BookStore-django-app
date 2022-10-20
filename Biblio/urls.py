from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns= [
    path('', inicio, name='inicio'),
    path('subir libro/', CrearLibro.as_view(), name='AgregarLibro'),
    path('registrarse/', registro, name='Registro'),
    path('inicio sesión/', iniciar_sesion, name='iniciarSesion'),
    path('agregar avatar/', agregarAvatar, name='agregarAvatar'),
    path('about', about, name='about'),
    path('listado libros/', VerLibros.as_view(), name='listaLibros'),
    path('resultados/', SearchLibro.as_view(), name='resultados'),
    path('mis libros/', MisLibros.as_view(), name='misLibros'),
    path('mis libros/editar/<int:pk>', LibroUpdate.as_view(), name='editarLibro'),
    path('mis libros/borrar/<int:pk>', LibroDelete.as_view(), name='borrarLibro'),
    path('logout', LogoutView.as_view(template_name='Biblio/logout.html'), name='Logout'),
    path('editar perfil', editarUsuario, name='editarUsuario'),

]
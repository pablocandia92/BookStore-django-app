from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import *


from .forms import FormularioRegistro
from . models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

#usuarioVer=''
# Vender libro
def inicio(request):
    
    return render(request, 'Biblio/inicio.html')

#solo usuarios logeados
class CrearLibro(LoginRequiredMixin, CreateView):
    
    model = ModelLibro
    success_url= reverse_lazy('inicio')
    fields=['nombre', 'autor', 'genero', 'idioma', 'precio', 'portada']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()
        return HttpResponseRedirect('../')
    #template_name='Biblio/crearlibro_form.html' #o crearlibro_form.html deberia llamarse como el modelo: modellibro_form.html

#Ver los libros

class VerLibros(ListView):

    model=ModelLibro
    #template_name='biblio/inicio.html'


#solo usuarios logeados
class MisLibros(LoginRequiredMixin, ListView):

    model=ModelLibro
    template_name='Biblio/misLibros.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)


#Registro
def registro(request):              

    if request.method=='POST':
        datosUser=FormularioRegistro(request.POST)

        if datosUser.is_valid():
            nombreUser = datosUser.cleaned_data['username']
            datosUser.save()

            return render(request, 'Biblio/inicio.html')
        
    else:
            datosUser = FormularioRegistro()

    return render(request, 'Biblio/registro.html', {'datos':datosUser})   
#Login
def iniciar_sesion(request):
    if request.method=='POST':
        datos=AuthenticationForm(request, data=request.POST)
        if datos.is_valid():
            usuario=datos.cleaned_data.get('username')
            contraseña=datos.cleaned_data.get('password')
            user=authenticate(username=usuario, password=contraseña)    

            if user:
                login(request, user)
                #usuarioVer=user
                return render(request, 'Biblio/inicio.html', {'mensaje':f'hola, {user}'}) 
            else:
                return render (request, 'Biblio/inicio.html', {'mensaje':f'Datos incorrectos'})                          

    else:
        datos=AuthenticationForm()
    
    return render (request, 'Biblio/login.html', {'datos':datos}) 

#solo usuarios logeados
@login_required
def editarUsuario(request):
    usuario=request.user
    if request.method=='POST':
        formUser=FormularioEditarUsuario(request.POST)
        if formUser.is_valid():
            info=formUser.cleaned_data

            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            
            usuario.save()

            return render (request, 'biblio/inicio.html')
    
    else:
        formUser=FormularioEditarUsuario(initial={'email':usuario.email})

    return render(request, 'biblio/editarPerfil.html', {'formUser':formUser, 'usuario': usuario})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':

        miFormulario= AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            u=User.objects.get(username=request.user)
            avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
            avatar.save()

            return render(request, 'Biblio/inicio.html')
    else:
        miFormulario=AvatarFormulario()

    return render(request, 'Biblio/agregarAvatar.html', {'miFormulario':miFormulario})


class LibroUpdate(LoginRequiredMixin, UpdateView):

    model=ModelLibro
    success_url= '../'
    fields=['nombre', 'autor', 'genero', 'idioma', 'precio', 'portada']

class LibroDelete(LoginRequiredMixin, DeleteView):

    model=ModelLibro
    success_url= '../'

class SearchLibro(ListView):

    model=ModelLibro
    template_name= 'resultados.html'

    def get_queryset(self):
        busqueda=self.request.GET.get('libro')
        libros= ModelLibro.objects.filter(nombre__icontains=busqueda)
        return libros

def about(request):

    return render(request, 'Biblio/about.html')

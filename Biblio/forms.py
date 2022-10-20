from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):

    email=forms.EmailField()

    password1: forms.CharField(label='Contraseña')
    password2: forms.CharField(label='Repita contraseña')

    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
        help_texts= {k:'' for k in fields}

class FormularioEditarUsuario(UserCreationForm):

    email=forms.EmailField(label='modificar email')
    password1=forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='repita contraseña', widget=forms.PasswordInput)
    imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model=User
        fields=['email', 'password1', 'password2']
        help_texts= {k:'' for k in fields}

class AvatarFormulario(forms.Form):

    
    imagen = forms.ImageField(required=True)
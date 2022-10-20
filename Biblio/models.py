from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
#from .views import usuario


# Create your models here.

bookGenres=[
    ('Ciencia ficción', 'Ciencia ficción'),
    ('Fantasía', 'Fantasía'),
    ('Aventura', 'Aventura'),
    ('Policial', 'Policial'),
    ('Novela histórica', 'Novela histórica'),
    ('Cuento', 'Cuento'),
    ('Obra de teatro', 'Obra de teatro'),
    ('Poesía', 'Poesía'),
    ('Misterio', 'Misterio'),
    ('Horror', 'Horror'), 
]

class ModelLibro(models.Model):

    nombre=models.CharField(max_length=60,
        null=False, blank=False)
    autor=models.CharField(max_length=60,
        null=False, blank=False    
    )
    genero=models.CharField(
        max_length=60,
        null=False, blank=False, 
        choices=bookGenres
    )
    idioma=models.CharField(max_length=20,
        null=False, blank=False
    )
    precio=models.FloatField(null=False, blank=False)
    portada=models.ImageField(upload_to='portadas',
        null=False, blank=False
    )
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    
    #settings.AUTH_USER_MODEL
    
    def __str__(self):
        return f'{self.nombre} - {self.autor}'
    


class Avatar(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to= 'avatares', null=True, blank=True)



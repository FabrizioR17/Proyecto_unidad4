from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Usuarios(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)


    class Meta:
        db_table = "Usuarios"

class Proyectos(models.Model):
    foto = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    tags = TaggableManager()
    url_proy = models.CharField(max_length=200)

    class Meta:
        db_table = "Proyectos"

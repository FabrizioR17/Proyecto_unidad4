from django.db import models

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
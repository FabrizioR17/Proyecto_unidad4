from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Proyectos

class NuevoUsuario(UserCreationForm):
  #ya trae usuario y 2 contras , solo le add el email
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name' , 'email', 'password1', 'password2' ]

    widgets = {'username':forms.TextInput(attrs={'class':'form-control mb-3'}),
              'first_name':forms.TextInput(attrs={'class':'form-control mb-3'}),
              'last_name':forms.TextInput(attrs={'class':'form-control mb-3'}),
              'email': forms.TextInput(attrs={'class':'form-control mb-3'}),
              'password1': forms.TextInput(attrs={'class':'form-control mb-3'}),
              'password2': forms.TextInput(attrs={'class':'form-control mb-3'})
              }

  def save (self , commit = True):
    user = super(NuevoUsuario, self).save(commit=False)
    user.email = self.cleaned_data['email']

    if commit:
      user.save()
    return user


class ProyForm(forms.ModelForm):

    class Meta:
        model = Proyectos
        fields = ['foto', 'titulo' , 'descripcion','tags','url_proy']

        widgets = {'foto':forms.TextInput(attrs={'class':'form-control mb-3'}),
          'titulo':forms.TextInput(attrs={'class':'form-control mb-3'}),
          'descripcion':forms.Textarea(attrs={'class':'form-control mb-3'}),
          'tags': forms.TextInput(attrs={'class':'form-control mb-3'}),
          'url_proy': forms.TextInput(attrs={'class':'form-control mb-3'})
          }
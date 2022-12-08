from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class NuevoUsuario(UserCreationForm):
  #ya trae usuario y 2 contras , solo le add el email
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name' , 'email', 'password', 'password2' ]

  def save (self , commit = True):
    user = super(NuevoUsuario, self).save(commit=False)
    user.email = self.cleaned_data['email']

    if commit:
      user.save()
    return user
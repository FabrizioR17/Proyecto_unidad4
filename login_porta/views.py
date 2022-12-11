from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from .forms import NuevoUsuario
from .models import Usuarios


from django.contrib.auth.mixins import LoginRequiredMixin #para clases
from django.contrib.auth.decorators import login_required #para funciones
# Create your views here.

class Principal(View):
  def get(self,request):
    template_name = 'login/main.html'
    return render(request, template_name)

class Registrar(CreateView):
  model = Usuarios
  form_class = NuevoUsuario
  template_name = 'registration/register.html'

  def form_valid(self, form):
    form.save
    Usuarios.objects.create(**form.cleaned_data)
    return redirect('login')
from django.shortcuts import render, redirect 
from django.views.generic import View, CreateView
from .forms import NuevoUsuario,ProyForm
from .models import Usuarios,Proyectos
from django.contrib.auth import login, authenticate , logout
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
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

class RegistrarProy(CreateView):
  model = Proyectos
  form_class = ProyForm
  template_name = 'login/loged.html'

  def form_valid(self, form):
    form.save
    Proyectos.objects.create(**form.cleaned_data)
    return redirect('login')


def loginPage(request):

  if request.method == 'POST':

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username , password=password)

    if user is not None:
      login(request, user)
      return redirect('loged')
    
    else:
      messages.info(request, 'username or password is incorrect')

  context = {}
  return render(request, 'registration/login.html', context )


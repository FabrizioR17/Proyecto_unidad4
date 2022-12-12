from django.urls import path
from . import views
from django.contrib.auth.views import  logout_then_login

urlpatterns = [
    path('', views.Principal.as_view(), name="principal"),
    path('accounts/login/', views.loginPage, name="login"),
    path('register/', views.Registrar.as_view(), name="register"),
    path('loged/', views.RegistrarProy.as_view() , name='loged'),
    path('logout/', logout_then_login, name="logout"),
    
]


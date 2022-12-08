from django.urls import path
from . import views
from django.contrib.auth.views import LoginView , logout_then_login

urlpatterns = [
    path('', views.Principal.as_view(), name="principal"),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('register/', views.Registrar.as_view(), name="register"),
    path('logout/', logout_then_login, name="logout"),
]


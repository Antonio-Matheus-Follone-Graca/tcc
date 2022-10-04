from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    # rotas 
    # index 
    path('',views.index, name="index"),
    # faz o método de logar
    path('logar',views.logar, name="logar"),
    # pagina do formulario de cadastrar 
    path('cadastrar',views.cadastrar,name="cadastrar"),
    # rota que faz o insert do usuario 
    path('insertUsuario',views.insertUsuario, name='insertUsuario'),
    path('dashboard',views.dashboard,name='dashboard'),
    # logout
    path('logout',views.logout, name='logout')
   

]
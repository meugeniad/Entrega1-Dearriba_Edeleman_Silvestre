from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('agregar-destino/', views.agregar_destino, name='agregar_destino'),
    path('about/', views.about, name='about'),
   
]

from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destino/listar/', views.listar, name='listar'),
    path('destino/agregar/', views.agregar_destino, name='agregar_destino'),
    path('destino/editar/<int:id>', views.editar_destino, name='editar_destino'),
    path('destino/eliminar/<int:id>', views.eliminar_destino, name='eliminar_destino'),
    path('destino/mostrar/<int:id>', views.mostrar_destino, name='mostrar_destino'),
    path('about/', views.about, name='about'),
   
]

from django.shortcuts import render
from home.models import Destino
from datetime import date


# Create your views here.

def crear_destino(request):
    
    destino = Destino(pais ='España', ciudad = 'Madrid', 
                      informacion = 'Es la capital del país. Tiene hermosas avenidas y parques. Museos: Nacional del Prado y Reina Sofía',
                      sugerido_para = 'La familia, turistas gastronómicos',
                      fecha_creacion = date.today(),
                      autor = 'Eugenia')
    destino.save()
    
    return render(request, 'crear_destino.html', {})

def listar(request):
    
    destinos = Destino.objects.all()
    
    return render(request, 'home/listar.html',{'destinos': destinos})

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

from django.shortcuts import render
from home.models import Destino


def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')


def listar(request):
    
    destinos = Destino.objects.all()
    
    return render(request, 'home/listar.html',{'destinos': destinos})

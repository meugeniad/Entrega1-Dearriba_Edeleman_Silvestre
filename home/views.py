from django.shortcuts import render
from home.models import Destino
from datetime import date


# Create your views here.

def agregar_destino(request):
   
    print(request.POST)
    # pais = request.POST.get('pais')
    # ciudad = request.POST.get('ciudad')
    # informacion =  request.POST.get('informacion')
    # sugerido_para =  request.POST.get('sugerido')
    # autor =  request.POST.get('autor')
    # destino = Destino(pais=pais, ciudad=ciudad, informacion=informacion,
    #                   sugerido_para=sugerido_para, fecha_creacion=date.today(),
    #                   autor=autor)
    # destino.save()
    
    return render(request, 'home/agregar_destino.html', {})

def listar(request):
    
    destinos = Destino.objects.all()
    
    return render(request, 'home/listar.html',{'destinos': destinos})

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

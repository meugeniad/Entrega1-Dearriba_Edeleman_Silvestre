from django.shortcuts import render, redirect
from django.urls import is_valid_path
from home.models import Destino
from datetime import date
from home.forms import DestinoFormulario , BuscarPaisFormulario


# Create your views here.

def agregar_destino(request):
   
    if request.method == "POST":
        
        formulario = DestinoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            pais = data['pais']
            ciudad = data['ciudad']
            informacion =  data['informacion']
            sugerido_para =  data['sugerido_para']
            autor =  data['autor']
            destino = Destino(pais=pais, ciudad=ciudad, informacion=informacion,
                            sugerido_para=sugerido_para, fecha_creacion=date.today(),
                            autor=autor)
            destino.save()
            
            return redirect('listar')
    
    formulario = DestinoFormulario()
    
    return render(request, 'home/agregar_destino.html', {'formulario': formulario})

def listar(request):
    
    pais = request.GET.get('pais',None)
    
    if pais: 
       destinos = Destino.objects.filter(pais__icontains=pais)
    else:  
        destinos = Destino.objects.all()
    
    formulario = BuscarPaisFormulario()
    
    return render(request, 'home/listar.html',{'destinos': destinos , 'formulario':formulario})

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

from django.shortcuts import render, redirect
from django.urls import is_valid_path
from home.models import Destino
from datetime import date
from home.forms import DestinoFormulario , BuscarPaisFormulario, EditarDestinoFormulario

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView


# Create your views here.
@login_required
def agregar_destino(request):
   
    if request.method == "POST":
        
        formulario = DestinoFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            pais = data['pais']
            ciudad = data['ciudad']
            informacion =  data['informacion']
            sugerido_para =  data['sugerido_para']
            autor =  data['autor']
            foto_destino = data['foto_destino']
            destino = Destino(pais=pais, ciudad=ciudad, informacion=informacion,
                            sugerido_para=sugerido_para, fecha_creacion=date.today(),
                            autor=autor,foto_destino=foto_destino)
            destino.save()
            
            return redirect('listar')
        else:
            return render(request, 'home/agregar_destino.html', {'formulario': formulario})
    
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



@login_required
def editar_destino(request, id):
    
    destino = Destino.objects.get(id=id)
    
    if request.method == "POST":
            
            formulario = EditarDestinoFormulario(request.POST, request.FILES)
            
            if formulario.is_valid():
                data = formulario.cleaned_data
            
                destino.pais = data['pais']
                destino.ciudad = data['ciudad']
                destino.informacion =  data['informacion']
                destino.sugerido_para =  data['sugerido_para']
                destino.autor =  data['autor']
                destino.foto_destino = data['foto_destino']
                destino.fecha_modificacion=date.today()
                destino.save()
                
                return redirect('listar')
            else:
                return render(request, 'home/editar_destino.html', {'formulario': formulario ,'destino':destino})
    else:    
        formulario = EditarDestinoFormulario(
            initial={
                'pais': destino.pais,
                'ciudad': destino.ciudad,
                'informacion' : destino.informacion,
                'sugerido_para' : destino.sugerido_para,
                'autor' : destino.autor,
                'foto_destino' :  destino.foto_destino
            }
        )
        
    return render(request, 'home/editar_destino.html', {'formulario': formulario ,'destino':destino})

@login_required
def eliminar_destino(request, id):
   destino = Destino.objects.get(id=id) 
   destino.delete()
   return redirect('listar')


# def mostrar_destino(request, id):
    
#     destino = Destino.objects.get(id=id)
           
#     formulario = DestinoFormulario(
#         initial={
#                 'pais': destino.pais,
#                 'ciudad': destino.ciudad,
#                 'informacion' : destino.informacion,
#                 'sugerido_para' : destino.sugerido_para,
#                 'autor' : destino.autor,
#                 'foto_destino' :  destino.foto_destino
#             }
#     )
        
#     return render(request, 'home/mostrar_destino.html', {'formulario': formulario ,'destino' : destino})

class MostrarDestino(DetailView):
    model = Destino
    template_name ='home/mostrar_destino_cbv.html'
    
   
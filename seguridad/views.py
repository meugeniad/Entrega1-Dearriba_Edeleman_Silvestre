from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from seguridad.forms import AltaUsuario


def mi_login(request):

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario) 
            return redirect('index')
    else:
        formulario = AuthenticationForm()

    return render(request, 'seguridad/login.html', {'formulario': formulario})


def registrar(request):

    if request.method == 'POST':
        formulario = AltaUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = AltaUsuario()

    return render(request, 'seguridad/registrar.html', {'formulario': formulario})

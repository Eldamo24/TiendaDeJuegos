from django.shortcuts import render
from Tienda.forms import *
from Tienda.models import * 

# Create your views here.

def vista_inicio(request):
    return render(request, "Tienda/index.html")

def vista_registro(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            user = Usuario(nombre = data["nombre"], apellido = data["apellido"], edad = data["edad"], email = data["email"], nombre_usuario = data["nombre_usuario"], contrasenia = data["contrasenia"])
            user.save()
    formulario = UsuarioForm()
    return render(request, "Tienda/registro.html", {"formulario": formulario})

def vista_juego(request):
    if request.method == "POST":
        formulario = JuegoForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            juego = Juego(nombre_juego = data["nombre_juego"], precio = data["precio"], sinopsis = data["sinopsis"])
            juego.save()
    formulario = JuegoForm()
    return render(request, "Tienda/juego.html", {"formulario": formulario})

def vista_consola(request):
    if request.method == "POST":
        formulario = ConsolaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            consola = Consola(nombre_consola = data["nombre_consola"], precio = data["precio"])
            consola.save()
    formulario = ConsolaForm()
    return render(request, "Tienda/consola.html", {"formulario": formulario})

def vista_inicio_sesion(request):
    return render(request, "Tienda/iniciar_sesion.html")

def vista_busqueda(request):
    return render(request, "Tienda/busqueda.html")

def vista_resultado(request):
    nombre_juego = request.GET["nombre_juego"]
    juego = Juego.objects.filter(nombre_juego__icontains=nombre_juego)
    return render(request, "Tienda/resultados_busqueda.html", {"juego": juego})
    
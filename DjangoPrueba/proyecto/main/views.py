from django.shortcuts import render, redirect

# Create your views here.

def inicio(request):
    return redirect('menuprincipal_wiki')

def registrase_wiki(request):
    return render(request, 'core/registrase_wiki.html')

def recuperarcontra(request):
    return render(request, 'core/recuperarcontra.html')

def micuentatf(request):
    return render(request, 'core/micuentatf.html')

def menuprincipal_wiki(request):
    return render(request, 'core/menuprincipal_wiki.html')

def Lugarestf(request):
    return render(request, 'core/Lugarestf.html')

def Logros(request):
    return render(request, 'core/Logros.html')

def inicio_sesion_wiki(request):
    return render(request, 'core/inicio_sesion_wiki.html')

def historia(request):
    return render(request, 'core/historia.html')

def forowiki(request):
    return render(request, 'core/forowiki.html')

def Flora(request):
    return render(request, 'core/Flora.html')

def Enemigos(request):
    return render(request, 'core/Enemigos.html')

def Consumibles(request):
    return render(request, 'core/Consumibles.html')

def Construcciones(request):
    return render(request, 'core/Construcciones.html')

def Armas(request):
    return render(request, 'core/Armas.html')

def Animales(request):
    return render(request, 'core/Animales.html')

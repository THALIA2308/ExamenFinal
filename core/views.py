from django.shortcuts import render
from .models import *
from core import models
from .models import Categorias
# Create your views here.

def inicio(request):
    return render(request, 'core/inicio.html')

def libro(request):
    libro = Libro.objects.all()
    context = {
        'libros' : libro 
    }
    return render(request, 'core/libro.html', context)

def lista_autores(request):
    autores = Autores.objects.all()
    return render(request, 'core/lista_autores.html', {'autores': autores})

def lista_categorias(request):
    categorias = Categorias.objects.all()
    return render(request, 'core/lista_categorias.html', {'categorias': categorias})
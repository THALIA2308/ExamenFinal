from django.urls import path
from .views import *

urlpatterns = [

    path('', inicio, name='inicio'),
    path('libro', libro, name='libro'),
    path('autores', lista_autores, name='lista_autores'),
    path('categorias/', lista_categorias, name='categorias'),
    path('cat/', lista_categorias, name='cat')
    
]
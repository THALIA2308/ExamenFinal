from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Libro)
admin.site.register(Autores)
admin.site.register(Categorias)
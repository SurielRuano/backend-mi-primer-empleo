from django.contrib import admin
from .models import Egresado, Carrera, Experiencia

# Register your models here.
admin.site.register(Egresado)
admin.site.register(Carrera)
admin.site.register(Experiencia)

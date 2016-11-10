from django.contrib import admin
from .models import Egresado, Carrera, Experiencia, Expectativa, EstSocioEcon

# Register your models here.
admin.site.register(Egresado)
admin.site.register(Carrera)
admin.site.register(Experiencia)
admin.site.register(Expectativa)
admin.site.register(EstSocioEcon)

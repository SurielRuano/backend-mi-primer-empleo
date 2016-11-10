from django.contrib import admin
from .models import BusinessModel, Vacante, Municipio, Solicitud, Expediente
# Register your models here.


class BusinessModelAdmin(admin.ModelAdmin):
	list_display = ('name', 'tel', 'email', 'name_project_manager',)
	search_fields = ('name', 'email',)
	ordering = ['name']

admin.site.register(BusinessModel, BusinessModelAdmin)
admin.site.register(Vacante)
admin.site.register(Municipio)
admin.site.register(Solicitud)
admin.site.register(Expediente)
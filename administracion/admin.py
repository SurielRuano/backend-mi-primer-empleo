from django.contrib import admin

from .models import sedeco, encuesta, reporteMensual
# Register your models here.

admin.site.register(sedeco)
admin.site.register(encuesta)
admin.site.register(reporteMensual)
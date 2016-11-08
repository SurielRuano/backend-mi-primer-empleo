from django.shortcuts import render
from django.core import serializers
from empresa.models import BusinessModel
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

class EmpresaJsonView (View):
	def get(self, request):
		cons = BusinessModel.objects.all()
		datos = serializers.serialize("json", cons),
		return HttpResponse(datos)
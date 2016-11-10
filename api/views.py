from django.shortcuts import render
from django.core import serializers
from empresa.models import BusinessModel, Vacante
from egresados.models import Egresado
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.utils.decorators import method_decorator


class EmpresaJsonView (View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(EmpresaJsonView, self).dispatch(request, *args, **kwargs)

	def get(self, request):
		cons = BusinessModel.objects.all()
		datos = serializers.serialize("json", cons),
		return HttpResponse(datos, content_type = 'application/javascript; charset=utf8')


class BecariosJsonView (View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(BecariosJsonView, self).dispatch(request, *args, **kwargs)

	def get(self, request):
		cons = Egresado.objects.all()
		datos = serializers.serialize("json", cons),
		return HttpResponse(datos, content_type = 'application/javascript; charset=utf8')


class VacantesJsonView (View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(VacantesJsonView, self).dispatch(request, *args, **kwargs)

	def get(self, request):
		cons = Vacante.objects.all()
		datos = serializers.serialize("json", cons),
		return HttpResponse(datos, content_type = 'application/javascript; charset=utf8')
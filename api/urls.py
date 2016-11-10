from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^empresas/$', views.EmpresaJsonView.as_view(), name="empresa"),
	url(r'^becarios/$', views.BecariosJsonView.as_view(), name="becarios"),
	url(r'^vacantes/$', views.VacantesJsonView.as_view(), name="vacantes"),
]
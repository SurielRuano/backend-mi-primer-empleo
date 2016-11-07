from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^empresa/$', views.EmpresaJsonView.as_view(), name="empresa"),
]
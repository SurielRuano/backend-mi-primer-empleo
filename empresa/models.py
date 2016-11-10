from django.db import models
from django.conf import settings
from egresados.models import Egresado


class Municipio(models.Model):

	municipio = models.CharField(max_length=200)
	region = models.CharField(max_length=5)
	estado = models.CharField(max_length=100)



# Create your models here.
class BusinessModel(models.Model):
	
	id_user = models.OneToOneField(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=150)
	street = models.CharField(max_length=100)
	colony = models.CharField(max_length=100)
	municipio = models.ForeignKey(Municipio)
	cpostal = models.IntegerField()
	adress_visits = models.TextField()
	tel = models.CharField(max_length=10)
	fax = models.CharField(max_length=20)
	email = models.EmailField()
	replegal = models.CharField(max_length=40)
	start_date = models.DateField()
	total_number_workes = models.IntegerField()
	giro = models.CharField(max_length=40)
	registry_date = models.DateField()
	name_project_manager = models.CharField(max_length=60)
	puesto = models.CharField(max_length=60)
	rfc = models.CharField(max_length=20)
	acteconomica = models.CharField(max_length=250)
	products_services = models.TextField()
	name_project = models.CharField(max_length=100)
	description = models.TextField()
	size = models.CharField(max_length=10)
	clasificacion = models.CharField(max_length=10)
	sectores = models.IntegerField()
	sector = models.CharField(max_length=10)
	rango_trab = models.CharField(max_length=60)
	acceso = models.CharField(max_length=60)
	extension = models.CharField(max_length=60)
	rfc_imagen = models.ImageField(upload_to='rfc_imagen')
	identificacion = models.CharField(max_length=60)
	identificacion_tutor =models.CharField(max_length=60)
	comprobante = models.CharField(max_length=60)
	carta =models.CharField(max_length=60)
	pagina = models.CharField(max_length=60)
	ubucacion =models.TextField()
	croquis = models.CharField(max_length=60)
	emailreproy = models.EmailField()
	validada = models.IntegerField()
	etapa = models.CharField(max_length=60)
	carpeta = models.IntegerField()
	administra = models.IntegerField()
	visto = models.IntegerField()


	def __str__(self):
		return self.name


class Vacante(models.Model):
	id_empresa = models.ForeignKey(BusinessModel, related_name='vacante')
	id_egresado = models.ForeignKey(Egresado, related_name='vacante', blank=True, null=True)
	puesto_solicitante = models.CharField(max_length=80)
	activades = models.TextField()
	dias = models.TextField()
	horario_entrada = models.CharField(max_length=50)
	horario_entrada_sabado = models.CharField(max_length=50, blank=True, null=True)
	horario_salida = models.CharField(max_length=50)
	horario_salida_sabado = models.CharField(max_length=50, blank=True, null=True)
	fecha_alta = models.CharField(max_length=50)
	fecha_asignado = models.CharField(max_length=50)
	vacante_activa = models.BooleanField(default=True)

	def __str__(self):
		return self.puesto_solicitante

class Solicitudes(models.Model):
	id_vacante = models.ForeignKey(Vacante, related_name='aspirante')
	id_egresado = models.ForeignKey(Egresado, related_name='aspirante')




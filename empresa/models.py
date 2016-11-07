from django.db import models
from django.conf import settings

# Create your models here.
class BusinessModel(models.Model):
	#id_mun = models.ForeignKey(Municipios, related_name='businessmodel')
	id_user = models.OneToOneField(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=150)
	street = models.CharField(max_length=100)
	colony = models.CharField(max_length=100)
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
	


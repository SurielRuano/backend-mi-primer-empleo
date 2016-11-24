from django.db import models
from egresados.models import Egresado

# Create your models here.

class Reportes(models.Model):
	egresado = models.ForeignKey(Egresado, related_name='reportes')
	numero = models.IntegerField()
	fecha = models.DateField()
	area = models.CharField(max_length=100)
	tutor = models.CharField(max_length=200)
	actividades = models.CharField(max_length=400)
	aporte = models.CharField(max_length=100)
	monto = models.CharField(max_length=10)
	capacitacion = models.BooleanField()
	en_que = models.BooleanField()
	proyecto =models.CharField(max_length=200)
	recursos = models.BooleanField()
	experiencia = models.BooleanField()
	emp_puntualidad = models.BooleanField()
	emp_imagen = models.BooleanField()
	emp_actitud = models.BooleanField()
	emp_aprendio = models.BooleanField()
	emp_objetivos_cump = models.BooleanField()
	validado= models.BooleanField()
	fecha_validacion = models.DateField()
	pago = models.BooleanField()
	fecha_pago = models.DateField()

	def __str__(self):
		return self.fecha
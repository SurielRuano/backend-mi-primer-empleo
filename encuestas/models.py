from django.db import models
from usuarios.models import Sedeco

# Create your models here.
class Encuesta(models.Model):
	id_sedeco = models.ForeignKey(Sedeco, related_name='encuesta')
	fecha_captura = models.DateField(auto_now=True)
	aporte = models.CharField(max_length=150)
	#por que medio se entero sobre la empresa Supongo
	#facebook, twitter, periodico, tv, radio, escuela, amigo, empresa, otro medio, 
	viade_informacion =  models.CharField(max_length=100)
	act_desemp = models.CharField(max_length=100)
	capacitacion = models.CharField(max_length=200)
	apoyo_extra = models.TextField()
	propuesta = models.TextField()
	contratado = models.BooleanField(default=True)
	motivo_no_contratacion = models.TextField()
	fecha_contrato = models.DateField(auto_now=True)
	salario = models.FloatField()
	evaluacion_experiencia = models.CharField(max_length=200)
	expectativas = models.TextField()
	mejora_programa = models.TextField()
	mejora_empresa = models.TextField()
	mejora_institucion = models.TextField()
	conocimientos = models.TextField()
	entrevista = models.TextField()
	oferta = models.TextField()
	lugar = models.TextField()

	def __str__(self):
		return self.id_sedeco






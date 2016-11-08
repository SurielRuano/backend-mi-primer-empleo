from django.db import models
from egresados.models import Egresado


class sedeco(models.Model):
	 nombre = models.CharField(max_length=100)
	 usuario = models.CharField(max_length=100)
	 clave = models.CharField(max_length=100)
	 acceso = models.IntegerField()
	 rol = models.IntegerField()
	 activate = models.IntegerField()
	 estado = models.IntegerField()


	 def __str__(self):

	 	return self.nombre

class encuesta(models.Model):

	 OPCIONES_D = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (PERIODICO, 'Periodico'),
        (TV, 'Tv'),
        (RADIO, 'Radio'),
        (ESCUELA, 'Escuela'),
        (AMIGO, 'Amigo'),
        (EMPRESA, 'Empresa'),
        (OTRO, 'Otro medio'),
    )

	sedeco = models.ForeignKey(sedeco null=True)
	fecha_captura = models.DateField()
	aporte = models.CharField(max_length = 200)
	medio_difusion_captado = models.CharField(max_length = 20,choices = OPCIONES_D)
	activ_perfil = models.BooleanField()
	medios_necesarios = models.BooleanField()
	capacitacion = models.BooleanField()
	apoyo_extra = models.BooleanField()
	contratado = models.BooleanField()
	razon_no_contratado = models.CharField(max_length=200)
	fecha_contratacion = models.DateField()
	salario = models.FloatField()
	prog_logro_espect= models.BooleanField()
	mejora_programa = models.CharField(max_length=400)
	mejora_empresa = models.CharField(max_length=400)
	mejora_institucion = models.CharField(max_length=400)
	cubrieron_necesidades = models.BooleanField()
	porque_no_necesidades = models.CharField(max_length=400)
	# conocimientos = models.BooleanField()
	# entrevista = models.BooleanField()
	# oferta = models.CharField()
	# lugar = models.CharField()


class reporteMensual(models.Model):

	egresado = models.ForeignKey(Egresado)
	# numero = models.IntegerField()
	fecha =models.DateField()
	area = models.CharField(max_length=200)
	tutor = models.CharField(max_length=200)
	actividades = models.CharField(max_length=200)
	aporte = models.CharField(max_length=200)
	monto = models.CharField(max_length=200)
	capacitacion = models.CharField(max_length=200)
	proyecto = models.CharField(max_length=200)
	puntualidad = models.CharField(max_length=200)
	capacitacion = models.CharField(max_length=200)
	recursos = models.BooleanField()
	experiencia = models.BooleanField()
	emp_puntualidad = models.BooleanField(blank=True,null=True)
	emp_imagen = models.BooleanField(blank=True,null=True)
	emp_actitud = models.BooleanField(blank=True,null=True)
	emp_aprendio = models.BooleanField(blank=True,null=True)
	emp_objetivos_cump = models.BooleanField(blank=True,null=True)
	validado= models.BooleanField()
	fecha_validacion = models.DateField()
	pago = models.BooleanField()
	fecha_pago = models.DateField()
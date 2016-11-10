from django.db import models

# Create your models here.
MASCULINO = 'M'
FEMENINO = 'F'
SEXO = (
	(MASCULINO, 'Masculino'), 
	(FEMENINO, 'Femenino'), 
	)
	


class Carrera (models.Model):

	nombre = models.CharField(max_length=100)
	#nivel = ???
	#area = ???
	#sectores = ???
	#validada = ???
	def __str__ (self):
		return self.nombre

class Egresado(models.Model):

	nombre = models.CharField(max_length=50, null=True, blank=True)
	apellidop = models.CharField(max_length=50, null=True, blank=True)
	apellidom = models.CharField(max_length=50, null=True, blank=True)
	edad = models.IntegerField(null=True, blank=True)
	#lugar = ???
	sexo = models.CharField(max_length=1, choices=SEXO, default=MASCULINO, null=True, blank=True)
	curp = models.CharField(max_length=18, null=True, blank=True)
	#municipio = moodels.OneToOneField(Municipio)
	calle = models.CharField(max_length=50, null=True, blank=True)
	#no = ???
	colonia = models.CharField(max_length=50, null=True, blank=True)
	fechaentregatitulo = models.DateField(auto_now_add=True, null=True, blank=True)
	cp = models.IntegerField(null=True, blank=True)
	telefonofijo = models.IntegerField( null=True, blank=True)
	celular = models.IntegerField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	#nivel = ???
	estudioen = models.CharField(max_length=100, null=True, blank=True)
	carrera = models.OneToOneField(Carrera, null=True, blank=True)
	#situacion = ???
	añoegreso = models.DateField(auto_now_add=True, null=True, blank=True)
	fechaingresoprograma = models.DateField(auto_now_add=True, null=True, blank=True)
	#colocado = ???
	certificado = models.FileField(upload_to = "certificado", null=True, blank=True)
	identificacion = models.FileField(upload_to = "identificación", null=True, blank=True)
	compdomicilio = models.FileField(upload_to = "domicilio", null=True, blank=True)
	titulo = models.FileField(upload_to = "titulo", null=True, blank=True)
	fcurp = models.FileField(upload_to = "curp", null=True, blank=True)
	carta = models.FileField(upload_to = "carta", null=True, blank=True)
	fechatitulacion = models.DateField(auto_now_add=True, null=True, blank=True)
	promedio = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
	becario = models.BooleanField("Es Becario",default= False)
	#modalidadtitulo = ???
	#empleoformal = ???
	#empleocual = ???
	#municipios = Repetido
	#sectores = #
	#compromiso = #
	#folio 
	#perfil
	rfc = models.CharField(max_length=13, null=True, blank=True)
	#status
	#motivobaja = ???
	#idvacante = #
	curriculum = models.FileField(upload_to = "cv", null=True, blank=True)
	#psicologica ???
	archivopsicologica = models.FileField(upload_to = "psico", null=True, blank=True)
	#notarjeta = ???
	#noseguropopular = ???
	#segpop = ???
	#traslado = ???
	#etapa = 
	#horaps
	#inicio
	#validada
	#userid
	#visto
	#carpeta
	#concluye

	def __str__ (self):
		return self.nombre


#class Expediente(models.Model):

class Experiencia(models.Model):

	puesto = models.CharField(max_length=100)
	#fecha = ???
	empresa = models.CharField(max_length=100)
	actividades = models.TextField()

	def __str__ (self):
		return self.puesto

#class Expectativa(models.Model):

#class Habilidad(models.Model):



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

	nombre = models.CharField(max_length=50, null=True)
	apellidop = models.CharField(max_length=50, null=True)
	apellidom = models.CharField(max_length=50, null=True)
	edad = models.IntegerField(null=True)
	#lugar = ???
	sexo = models.CharField(max_length=1, choices=SEXO, default=MASCULINO, null=True)
	curp = models.CharField(max_length=18, null=True)
	#municipio = moodels.OneToOneField(Municipio)
	calle = models.CharField(max_length=50, null=True)
	#no = ???
	colonia = models.CharField(max_length=50, null=True)
	fechaentregatitulo = models.DateField(auto_now_add=True, null=True)
	cp = models.IntegerField(null=True)
	telefonofijo = models.IntegerField( null=True)
	celular = models.IntegerField(null=True)
	email = models.EmailField(null=True)
	#nivel = ???
	estudioen = models.CharField(max_length=100, null=True)
	carrera = models.OneToOneField(Carrera, null=True)
	#situacion = ???
	añoegreso = models.DateField(auto_now_add=True, null=True)
	fechaingresoprograma = models.DateField(auto_now_add=True, null=True)
	#colocado = ???
	certificado = models.FileField(upload_to = "certificado", null=True)
	identificacion = models.FileField(upload_to = "identificación", null=True)
	compdomicilio = models.FileField(upload_to = "domicilio", null=True)
	titulo = models.FileField(upload_to = "titulo", null=True)
	fcurp = models.FileField(upload_to = "curp", null=True)
	carta = models.FileField(upload_to = "carta", null=True)
	fechatitulacion = models.DateField(auto_now_add=True, null=True)
	promedio = models.DecimalField(decimal_places=2, max_digits=2, null=True)
	#modalidadtitulo = ???
	#empleoformal = ???
	#empleocual = ???
	#municipios = Repetido
	#sectores = #
	#compromiso = #
	#folio 
	#perfil
	rfc = models.CharField(max_length=13, null=True)
	#status
	#motivobaja = ???
	#idvacante = #
	curriculum = models.FileField(upload_to = "cv", null=True)
	#psicologica ???
	archivopsicologica = models.FileField(upload_to = "psico", null=True)
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



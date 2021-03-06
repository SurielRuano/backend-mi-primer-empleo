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
	nivel = models.CharField(max_length=200)
	area = models.CharField(max_length=200)	
	sectores = models.CharField(max_length=20)	
	validada = models.BooleanField(default=False)
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
	#municipio = models.ForeignKey(Municipio)
	calle = models.CharField(max_length=50, null=True, blank=True)
	numero = models.IntegerField()
	colonia = models.CharField(max_length=50, null=True, blank=True)
	fechaentregatitulo = models.DateField(auto_now_add=True, null=True, blank=True)
	cp = models.IntegerField(null=True, blank=True)
	telefonofijo = models.IntegerField( null=True, blank=True)
	celular = models.IntegerField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	#nivel = ???
	estudioen = models.CharField(max_length=100, null=True, blank=True)
	carrera = models.ForeignKey(Carrera, null=True, blank=True)
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


 

class Experiencia(models.Model):

	id_egresado = models.ForeignKey(Egresado)
	puesto = models.CharField(max_length=100)	
	fecha = models.DateField()
	empresa = models.CharField(max_length=100)
	actividades = models.TextField()

	def __str__ (self):
		return self.puesto

class Expectativa(models.Model):

	id_egresado = models.OneToOneField(Egresado)
	entrevista_lab = models.BooleanField()
	que_quieres = models.CharField(max_length=100)	
	que_esperas = models.CharField(max_length=100)
	uso_beca = models.CharField("Que haras con la beca?",max_length=100)
	aportacion = models.TextField(max_length=100)
	logro = models.TextField("Objetivo Profesional",max_length=100)
	logro_academico = models.CharField("Objetivo Academico",max_length=100)
	formacion = models.CharField("Objetivo Academico",max_length=20)
	eleccion_correcta = models.BooleanField()
	gasto_mensual = models.CharField(max_length=80)
	empleo_buscado = models.BooleanField("Buscaste empleo")
	tiempo_busqueda = models.CharField("Cuanto tiempo",max_length=80)
	medios_busqueda = models.CharField("Que medios usaste para buscar",max_length=80)
	


class EstSocioEcon(models.Model):

	EDOC = (
	(MASCULINO, 'Masculino'), 
	(FEMENINO, 'Femenino'), 
	)

	id_egresado = models.OneToOneField(Egresado)
	edo_civil = models.CharField(max_length=50,choices = EDOC)
	dependientes = models.CharField(max_length=2)
	situacionlaboral = models.CharField(max_length=20)
	trabajo = models.CharField(max_length=30)
	dependen_ti = models.BooleanField("Alguien depende de ti?")
	cuantos_depend = models.IntegerField("Cuantos dependen de ti")
	ingreso_mensual = models.CharField(max_length=20)
	transporte = models.BooleanField()
	vives_en = models.CharField(max_length=60)
	cuantos_hermanos = models.CharField(max_length=20)
	cuantos_papas = models.CharField(max_length=20)
	cuantos_abuelos = models.CharField(max_length=20)
	casa_techo = models.CharField(max_length=20)
	casa_piso = models.CharField(max_length=20)
	casa_pared = models.CharField(max_length=20)
	numero_recamaras = models.CharField(max_length=20)
	numero_banos = models.IntegerField()
	numero_salas = models.IntegerField()	
	numero_comedor = models.CharField(max_length=20)
	numero_vehiculos =   models.IntegerField()	
	numero_recamaras =  models.IntegerField()
	gasto_mensual = models.CharField(max_length=20)
	mayor_gasto = models.CharField(max_length=20)
	otra_beca = models.BooleanField()





#class Habilidad(models.Model):



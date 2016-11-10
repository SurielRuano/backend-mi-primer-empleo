from django.db import models
from django.conf import settings

# Create your models here.
class Sedeco(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	acceso = models.IntegerField()
	rol = models.CharField(max_length=80)
	activate = models.BooleanField(default=True)
	estado = models.CharField(max_length=80)
	ip = models.CharField(max_length=15)

	def __str__(self):
		return self.user



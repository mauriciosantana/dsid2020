from jsonfield import JSONField
from django.db import models

class Turismo(models.Model):
	nome_cidade = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.nome_cidade

	def date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')

class Hotel(models.Model):
	fields = JSONField(blank=True, null=True)

	def __str__(self):
		return self.fields

class Voo(models.Model):
	fields = JSONField(blank=True, null=True)

	def __str__(self):
		return self.fields

from django.db import models

class Turismo(models.Model):
	nome_cidade = models.CharField(max_length=100)
	date = models.DateTimeField()
	
	def __str__(self):
		return self.nome_cidade

	def date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')

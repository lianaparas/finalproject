from django.db import models

# Create your models here.

class Location(models.Model):
	locat		= models.CharField(max_length=150)
	total 		= models.IntegerField(default=20)

	def __str__(self):
		return self.name

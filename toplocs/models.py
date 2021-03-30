from django.db import models

# Create your models here.
class Locsdata(models.Model):
    locat = models.TextField(blank=True, primary_key=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locsdata'

        def __str__(self):
        	return "{}-{}".format(self.locat, self.total)
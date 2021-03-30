from django.db import models

# Create your models here.
class TotalTwCategory(models.Model):
    name 		= models.TextField(blank=True, primary_key=True)
    economic 	= models.IntegerField(blank=True, null=True)
    environment = models.IntegerField(blank=True, null=True)
    health 		= models.IntegerField(blank=True, null=True)
    total 		= models.IntegerField(blank=True, null=True)

    class Meta:
        #managed 	= False (Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table)
        db_table 	= 'total_tw_category'

class FinalCategory(models.Model):
    name = models.TextField(blank=True, primary_key=True)
    category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_category'

class OriginTwt(models.Model):
    user_screen_name = models.TextField(blank=True, primary_key=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'origin_twt'
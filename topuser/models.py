from django.db import models

# Create your models here.
class TopTwsScore(models.Model):
    user_screen_name = models.TextField(blank=True, primary_key=True)
    text 			 = models.TextField(blank=True, null=True)
    favorite_count 	 = models.IntegerField(blank=True, null=True)
    retweet_count 	 = models.IntegerField(blank=True, null=True)
    scores 			 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed		= False
        db_table 	= 'top_tws_score'


class TopUserVolume(models.Model):
    name 			= models.TextField(blank=True, primary_key=True)
    economic		= models.IntegerField(blank=True, null=True)
    environment 	= models.IntegerField(blank=True, null=True)
    health 			= models.IntegerField(blank=True, null=True)
    total 			= models.IntegerField(blank=True, null=True)

    class Meta:
        managed 	= False
        db_table 	= 'top_user_volume'


class TopUserEco(models.Model):
    name 			= models.TextField(blank=True, primary_key=True)
    eco_score 		= models.IntegerField(blank=True, null=True)

    class Meta:
        #managed 	= False (Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table)
        db_table 	= 'top_user_eco'

        def __str__(self):
            return "{}-{}".format(self.name, self.eco_score)


class TopUserEnv(models.Model):
    name 			= models.TextField(blank=True, primary_key=True)
    env_score 		= models.IntegerField(blank=True, null=True)

    class Meta:
        #managed 	= False
        db_table 	= 'top_user_env'

        def __str__(self):
            return "{}-{}".format(self.name, self.env_score)


class TopUserHealth(models.Model):
    name 			= models.TextField(blank=True, primary_key=True)
    health_score 	= models.IntegerField(blank=True, null=True)

    class Meta:
        #managed 	= False
        db_table 	= 'top_user_health'

        def __str__(self):
            return "{}-{}".format(self.name, self.health_score)

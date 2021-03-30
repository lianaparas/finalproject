from django.db import models

# Create your models here.

class SnaReplies(models.Model):
    source = models.TextField(db_column='Source', primary_key=True)  # Field name made lowercase.
    target = models.TextField(db_column='Target', blank=True, null=True)  # Field name made lowercase.
    strength = models.IntegerField(db_column='Strength', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sna_replies_edges'
# Generated by Django 3.1.5 on 2021-03-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0005_auto_20210313_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='location',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='location',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='location',
            name='place',
        ),
        migrations.AddField(
            model_name='location',
            name='total',
            field=models.IntegerField(default=20),
        ),
    ]

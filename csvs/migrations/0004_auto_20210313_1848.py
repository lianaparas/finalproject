# Generated by Django 3.1.5 on 2021-03-13 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0003_auto_20210313_1847'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Maps',
            new_name='Location',
        ),
    ]
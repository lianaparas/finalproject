# Generated by Django 3.1.5 on 2021-03-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locsdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locat', models.TextField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'locsdata',
                'managed': False,
            },
        ),
    ]

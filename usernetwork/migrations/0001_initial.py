# Generated by Django 3.1.5 on 2021-03-23 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnaReplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField(blank=True, db_column='Source', null=True)),
                ('target', models.TextField(blank=True, db_column='Target', null=True)),
                ('strength', models.IntegerField(blank=True, db_column='Strength', null=True)),
            ],
            options={
                'db_table': 'sna_replies_edges',
                'managed': False,
            },
        ),
    ]

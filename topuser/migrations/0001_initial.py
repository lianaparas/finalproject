# Generated by Django 3.1.5 on 2021-03-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopTwsScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_screen_name', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('favorite_count', models.IntegerField(blank=True, null=True)),
                ('retweet_count', models.IntegerField(blank=True, null=True)),
                ('scores', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'top_tws_score',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TopUserVolume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('economic', models.IntegerField(blank=True, null=True)),
                ('environment', models.IntegerField(blank=True, null=True)),
                ('health', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'top_user_volume',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TopUserEco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('eco_score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'top_user_eco',
            },
        ),
        migrations.CreateModel(
            name='TopUserEnv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('env_score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'top_user_env',
            },
        ),
        migrations.CreateModel(
            name='TopUserHealth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('health_score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'top_user_health',
            },
        ),
    ]

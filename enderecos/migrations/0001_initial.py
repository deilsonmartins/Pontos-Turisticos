# Generated by Django 3.1.5 on 2021-01-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha1', models.TextField(max_length=150)),
                ('linha2', models.TextField(blank=True, max_length=150, null=True)),
                ('cidade', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=150)),
                ('pais', models.CharField(max_length=70)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

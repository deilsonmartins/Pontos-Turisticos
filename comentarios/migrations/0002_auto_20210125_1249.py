# Generated by Django 3.1.5 on 2021-01-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_pelicula_delete_peliculas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.DurationField(null=True),
        ),
    ]

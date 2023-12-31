# Generated by Django 4.2.3 on 2023-07-25 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_alter_pelicula_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudAmistad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to=settings.AUTH_USER_MODEL)),
                ('recipiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipiente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

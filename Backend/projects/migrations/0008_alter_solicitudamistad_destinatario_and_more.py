# Generated by Django 4.2.3 on 2023-07-25 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudamistad',
            name='destinatario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to='projects.usuario'),
        ),
        migrations.AlterField(
            model_name='solicitudamistad',
            name='recipiente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipiente', to='projects.usuario'),
        ),
    ]

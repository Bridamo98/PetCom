# Generated by Django 2.2.4 on 2019-11-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_de_mascotas', '0016_auto_20191113_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='esterilizado',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default=None, max_length=3),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='tamanio',
            field=models.CharField(choices=[('', '---------'), ('Enano', 'Enano'), ('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande'), ('Gigante', 'Gigante')], max_length=9),
        ),
    ]
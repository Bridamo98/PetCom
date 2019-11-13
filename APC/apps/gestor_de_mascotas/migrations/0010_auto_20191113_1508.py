# Generated by Django 2.2.4 on 2019-11-13 20:08

import apps.gestor_de_mascotas.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_de_mascotas', '0009_auto_20191110_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedad2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='mascota',
            name='fecha_nacimiento',
            field=models.DateField(validators=[apps.gestor_de_mascotas.models.validate_current_century], verbose_name='Fecha nacimiento'),
        ),
    ]

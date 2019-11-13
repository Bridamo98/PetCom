# Generated by Django 2.2.4 on 2019-11-13 22:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_de_mascotas', '0014_auto_20191113_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='peso',
            field=models.PositiveIntegerField(default=None, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='color',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 2.2.4 on 2019-11-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_de_mascotas', '0019_auto_20191117_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(blank=True, default='images/anonimo.jpg', null=True, upload_to='images/'),
        ),
    ]
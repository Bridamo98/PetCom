# Generated by Django 2.2.4 on 2019-11-16 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0010_auto_20191115_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento_global',
            name='tipo_evento',
            field=models.CharField(choices=[('Adopción', 'Adopción'), ('Esterilización', 'Esterilización'), ('Vacunación', 'Vacunación'), ('Feria de mascotas', 'Feria de mascotas')], max_length=256),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='tipo_lugar',
            field=models.CharField(choices=[('Clínicas veterinarias', 'Clínicas veterinarias'), ('Consultorios veterinarios', 'Consultorios veterinarios'), ('Refugios', 'Refugios'), ('Centros de adopción', 'Centros de adopción'), ('Fundaciones', 'Fundaciones'), ('Guarderías', 'Guarderias'), ('Sitio Pet Friendly', 'Sitio Pet Friendly'), ('Tiendas para mascotas', 'Tiendas para mascotas'), ('Spa para mascotas', 'Spa para mascotas')], max_length=256),
        ),
    ]

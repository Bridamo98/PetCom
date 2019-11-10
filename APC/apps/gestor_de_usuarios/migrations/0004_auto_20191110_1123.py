# Generated by Django 2.2.4 on 2019-11-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_de_usuarios', '0003_auto_20191101_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='topicos',
            field=models.ManyToManyField(blank=True, to='gestor_de_usuarios.Topico'),
        ),
    ]

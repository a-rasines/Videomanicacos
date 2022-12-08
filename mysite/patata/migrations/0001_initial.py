# Generated by Django 4.1.2 on 2022-12-08 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('url_p', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_salida', models.IntegerField()),
                ('pegi', models.IntegerField()),
                ('comanya', models.CharField(max_length=50)),
                ('url_v', models.URLField(default='')),
                ('url_banner', models.URLField(default='')),
                ('featured', models.BooleanField(default=False)),
                ('description', models.TextField(default='')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patata.genero')),
                ('plataforma', models.ManyToManyField(to='patata.plataforma')),
            ],
        ),
    ]

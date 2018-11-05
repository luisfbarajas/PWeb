# Generated by Django 2.1.2 on 2018-11-05 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actividades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('duracion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('puesto', models.CharField(max_length=255)),
                ('carrera', models.CharField(max_length=255)),
                ('antiguedad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lider', models.CharField(max_length=255)),
                ('inicia', models.DateField(auto_now_add=True)),
                ('duracion', models.IntegerField()),
                ('reuniones', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='actividades',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.empleados'),
        ),
    ]
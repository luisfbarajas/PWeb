# Generated by Django 2.1.2 on 2018-11-05 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroproyecto',
            name='trabaja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.empleados'),
        ),
        migrations.AlterField(
            model_name='registroproyecto',
            name='inicia',
            field=models.DateField(),
        ),
    ]

# Generated by Django 2.1.3 on 2018-11-30 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_auto_20181130_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroproyecto',
            name='ObjGeneral',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='registroproyecto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
# Generated by Django 2.1.3 on 2018-11-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_auto_20181130_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroproyecto',
            name='ObjGeneral',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

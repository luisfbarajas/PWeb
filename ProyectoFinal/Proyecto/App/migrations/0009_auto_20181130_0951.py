# Generated by Django 2.1.3 on 2018-11-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20181130_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroproyecto',
            name='departamento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
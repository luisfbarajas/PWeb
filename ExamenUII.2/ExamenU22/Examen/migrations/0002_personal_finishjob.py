# Generated by Django 2.1.2 on 2018-10-08 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='finishJob',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
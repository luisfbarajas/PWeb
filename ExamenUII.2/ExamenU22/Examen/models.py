from django.db import models

# Create your models here.
class Activities(models.Model):
    actName = models.CharField(max_length=255)
    lead = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    start =  models.DateField()
    end = models.DateField()

    class Meta:
        db_table='Activities'

    def __str__(self):
        return self.actName
class Personal(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    jobTeam = models.CharField(max_length=255)
    activitie = models.ForeignKey(Activities, on_delete = models.CASCADE)
    finishJob = models.IntegerField()
    class Meta:
         db_table = 'Personal'

    def __str__(self):
        return self.name


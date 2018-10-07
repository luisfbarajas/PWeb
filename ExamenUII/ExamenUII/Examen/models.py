from django.db import models

# Create your models here.
class Palco(models.Model):
    Category = models.CharField(max_length = 255)
    palcoName = models.CharField(max_length = 255)
    capacity = models.IntegerField()
    location =  models.CharField(max_length = 255)
    class Meta:
        db_table = "Palco"

    def __str__(self):
        return self.palcoName

class seat(models.Model):
    number = models.IntegerField()
    location = models.CharField(max_length = 255)
    Category = models.CharField(max_length = 255)

    class Meta:
        db_table = 'seat'
    def __str__(self):
        return str(self.number)

class Fanatics(models.Model):
    name= models.CharField(max_length=255)
    age =models.IntegerField()
    adress = models.CharField(max_length = 255)
    team = models.CharField(max_length = 255)
    palco = models.ForeignKey(Palco, on_delete= models.CASCADE)
    dateFan = models.DateTimeField(auto_now_add=True)
    seat = models.ForeignKey(seat, on_delete = models.CASCADE)

    class Meta:
        db_table = 'fanatics'

    def __str__(self):
        return self.name

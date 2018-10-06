from django.db import models


class Team(models.Model):
    # Id = models.AutoField(primary_key=True)
    NameTeam = models.CharField(max_length = 255)
    NumberPlayers = models.IntegerField()
    foundation = models.IntegerField()
    owner =  models.CharField(max_length = 255)
    divition =  models.CharField(max_length = 255)



class Player(models.Model):
    # Id = models.AutoField(primary_Key = True)
    Id_Team = models.ForeignKey(Team, on_delete = models.CASCADE)
    NamePlayer = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255)
    experience = models.CharField(max_length = 255)
    heigth = models.IntegerField()
    Age = models.IntegerField()
    weigth = models.IntegerField()

class Stadium(models.Model):
    # Id = models.AutoField(primary_key = True)
    Id_Team = models.ForeignKey(Team, on_delete = models.CASCADE)
    NameStadium = models.CharField(max_length = 255)
    Location = models.CharField(max_length = 255)
    owner = models.CharField(max_length = 255)
    opening = models.CharField(max_length = 255)
    capacity = models.IntegerField()

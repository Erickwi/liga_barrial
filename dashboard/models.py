from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()

class Result(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    winner = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.CharField(max_length=50)

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=100)

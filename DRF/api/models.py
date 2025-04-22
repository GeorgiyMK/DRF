from django.db import models

class Weapon(models.Model):
    power = models.IntegerField()
    rarity = models.CharField()
    value = models.IntegerField()


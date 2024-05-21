from django.db import models
from django.conf import settings

from players.models import Players
from campaigns.models import Campaigns

# Create your models here.

class SavageWorlds(models.Model):

  adventurer_name = models.CharField(max_length=50)
  player_name = models.ForeignKey(Players, related_name="SavageWorlds_Players", on_delete=models.PROTECT)
  campaign = models.ForeignKey(Campaigns, related_name="SavageWorlds_Campaigns", on_delete=models.PROTECT)
  character_name = models.CharField(max_length=50)
  xp = models.IntegerField(default=0)
  rank = models.CharField(max_length=3, choices=(('nov','novice'),('sea','seasoned'),('vet','veteran'),('her','heroic'),('leg','legendary')))
  description = models.TextField(null=True,blank=True)
  status = models.CharField(max_length=30, null=True, blank=True)
  bennies = models.IntegerField(default=0)
  convinction = models.TextField(null=True,blank=True)
  agility = models.IntegerField(default=4)
  smarts = models.IntegerField(default=4)
  spirit = models.IntegerField(default=4)
  strength = models.IntegerField(default=4)
  vigor = models.IntegerField(default=4)
  charisma = models.IntegerField(default=0)
  pace = models.IntegerField(default=0)
  parry = models.IntegerField(default=4)
  reason = models.IntegerField(default=0)
  toughness = models.IntegerField(default=4)
  hindrances = models.JSONField({})
  edges = models.JSONField({})
  skills = models.JSONField({})
  armour = models.JSONField({})
  weapons = models.JSONField({})
  possessions = models.JSONField({})
  extra_equipments = models.JSONField({})
  power = models.IntegerField(default=0)
  wounds = models.IntegerField(default=0)
  fatigue = models.IntegerField(default=0)
  bullets = models.JSONField({})

  class Meta:
    managed = True
    db_table = "savage_worlds"

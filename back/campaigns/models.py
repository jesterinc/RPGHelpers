from django.db import models
from django.conf import settings

from players.models import Players
from role_systems.models import RoleSystems

# Create your models here.

class Campaigns(models.Model):

  name = models.CharField(max_length=150)
  role_system = models.ForeignKey(RoleSystems, related_name="Campaigns_RoleSystems", on_delete=models.PROTECT)
  master = models.ManyToManyField(Players, related_name="Campaigns_Players")
  start_date = models.DateField()
  available_seats = models.IntegerField(default=0)
  max_seats = models.IntegerField(default=1)
  weekday_fixed = models.BooleanField(default=False)
  playing_weekdays = models.JSONField({"Mon": False, "Tue": False, "Wed": False, "Thu": False, "Fri": False, "Sat": False, "Sun": False}, null=True,blank=True)
  multi_seat = models.BooleanField(default=False)
  active = models.BooleanField(default=True)
  deleted = models.BooleanField(default=False)

  class Meta:

    managed = True
    db_table = "campaigns"
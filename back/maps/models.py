from django.db import models

# Create your models here.

from campaigns.models import Campaigns


class Maps(models.Model): 

  map_name = models.ImageField(upload_to="maps")
  campaign = models.ForeignKey(Campaigns, related_name="Maps_Campaigns", on_delete=models.PROTECT)
  actual = models.BooleanField(default=False)  #
  active = models.BooleanField(default=True)
  deleted = models.BooleanField(default=False)

  class Meta:

    managed = True
    db_table = "maps"


class Obstacles(models.Model):

  obstacle = models.CharField(max_length=100)
  map_ref = models.ForeignKey("Maps", related_name="Obstacles_Maps", on_delete=models.PROTECT)
  pos_x = models.IntegerField(default=0)
  pos_y = models.IntegerField(default=0)
  active = models.BooleanField(default=True)
  deleted = models.BooleanField(default=False)

  class Meta:

    managed = True
    db_table = "obstacles"


class Protections(models.Model):

  protection = models.CharField(max_length=100)
  map_ref = models.ForeignKey("Maps", related_name="Protections_Maps", on_delete=models.PROTECT)
  pos_x = models.IntegerField(default=0)
  pos_y = models.IntegerField(default=0)
  protection_factor = models.ForeignKey("ProtectionsFactors", related_name="Protections_ProtectionFactors", on_delete=models.PROTECT)
  cell_size = models.IntegerField(default=45)
  active = models.BooleanField(default=True)
  deleted = models.BooleanField(default=False)

  class Meta:

    managed = True
    db_table = "protections"


class ProtectionsFactors(models.Model):

  protection_factor = models.CharField(max_length=30)
  protection_factor_value = models.IntegerField(default=0)
  active = models.BooleanField(default=True)
  deleted = models.BooleanField(default=False)

  class Meta:

    managed = True
    db_table = "protections_factors"

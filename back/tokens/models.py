from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

from campaigns.models import Campaigns
from maps.models import Maps

class Tokens(models.Model):

  token = models.ImageField(upload_to="tokens")
  name = models.CharField(max_length=50, null=True,blank=True)
  campaign = models.ForeignKey(Campaigns, related_name="Tokens_Campaigns", on_delete=models.PROTECT)
  current_map = models.ForeignKey(Maps, related_name="Tokens_Maps", on_delete=models.PROTECT)
  current_position_x = models.IntegerField(default=0)
  current_position_y = models.IntegerField(default=0)
  direction = models.BooleanField(default=False)
  current_direction = models.CharField(max_length=2, choices=(('up','Up'), ('do','Down'), ('le','Left'), ('ri','Right'), ('ul','Up Left'), ('ur','Up Right'), ('dl','Down Left'), ('dr','Down Right')), null=True, blank=True)
  actual_fow_range = models.IntegerField(default=1)
  direction_fow = models.CharField(max_length=3, choices=(('fon','Front Only'), ('cir','circular'), ('fan','flat angle')), default='cir')
  active = models.BooleanField(default=True)
  deleted = models.BooleanField(default=False)
  history = HistoricalRecords()
  
  class Meta:

    managed = True
    db_table = "tokens"

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Players(models.Model):

  user = models.OneToOneField(User, related_name="Players_Users", on_delete=models.CASCADE)
  role = models.CharField(max_length=3, choices=(('ply','player'),('mtr','master'),('bth','both')))
  active = models.BooleanField(default=False)
  deleted = models.BooleanField(default=False)

  class Meta:

    managed = True
    db_table = "players"
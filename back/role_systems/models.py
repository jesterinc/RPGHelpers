from django.db import models
from django.conf import settings

# Create your models here.

class RoleSystems(models.Model):
  
  role_system = models.CharField(max_length=150)
  version = models.CharField(max_length=50)
  active = models.BooleanField(default=True)
  deleted = models.BooleanField(default=False)

  class Meta:
    managed = True
    db_table = "role_systems"


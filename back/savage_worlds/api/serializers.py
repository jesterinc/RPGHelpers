from rest_framework import serializers
from django.conf import settings
from savage_worlds.models import *
    

class SavageWorldsSerializer(serializers.ModelSerializer):

  class Meta:
    model=SavageWorlds
    fields="__all__"
      
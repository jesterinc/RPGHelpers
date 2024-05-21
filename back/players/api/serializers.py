from rest_framework import serializers
from django.conf import settings
from players.models import *
    

class PlayersSerializer(serializers.ModelSerializer):

  class Meta:
    model=Players
    fields="__all__"
      
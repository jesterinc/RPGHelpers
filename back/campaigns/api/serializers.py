from rest_framework import serializers
from django.conf import settings
from campaigns.models import *
    

class CampaignsSerializer(serializers.ModelSerializer):

  class Meta:
    model=Campaigns
    fields="__all__"
      
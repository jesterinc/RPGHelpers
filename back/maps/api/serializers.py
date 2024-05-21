from rest_framework import serializers
from rest_framework.serializers import  FileField

from django.conf import settings

from maps.models import *
from campaigns.models import Campaigns
from campaigns.api.serializers import CampaignsSerializer
    

class MapsSerializer(serializers.ModelSerializer):
  campaign = CampaignsSerializer(many=False, read_only=True)
  campaign_id = serializers.PrimaryKeyRelatedField(queryset=Campaigns.objects.all(), many=False)

  class Meta:
    model=Maps
    fields="__all__"


class MapWriteSerializer(serializers.ModelSerializer):

  class Meta:
    model=Maps
    fields='__all__'


class ObstaclesSerializer(serializers.ModelSerializer):
  map_ref = MapsSerializer(many=False, read_only=True)
  map_ref_id = serializers.PrimaryKeyRelatedField(queryset=Maps.objects.all(), many=False)

  class Meta:
    model=Obstacles
    fields="__all__"


class ProtectionsFactorsSerializer(serializers.ModelSerializer):

  class Meta:
    model=Protections
    fields="__all__"


class ProtectionsSerializer(serializers.ModelSerializer):
  map_ref = ProtectionsFactorsSerializer(many=False, read_only=True)
  map_ref_id = serializers.PrimaryKeyRelatedField(queryset=Maps.objects.all(), many=False)
  protection_factor = MapsSerializer(many=False, read_only=True)
  protection_factor_id = serializers.PrimaryKeyRelatedField(queryset=ProtectionsFactors.objects.all(), many=False)

  class Meta:
    model=Protections
    fields="__all__"



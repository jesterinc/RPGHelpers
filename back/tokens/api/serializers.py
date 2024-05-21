from rest_framework import serializers
from django.conf import settings

from tokens.models import Tokens
from maps.models import Maps
from maps.api.serializers import MapsSerializer
    

class TokensSerializer(serializers.ModelSerializer):
  map_ref = MapsSerializer(many=False, read_only=True)
  #map_ref_id = serializers.PrimaryKeyRelatedField(queryset=Maps.objects.all(), many=False)

  class Meta:
    model=Tokens
    fields="__all__"


class TokenWriteSerializer(serializers.ModelSerializer):

  class Meta:
    model=Tokens
    fields="__all__"


class TokenPositionSerializer(serializers.ModelSerializer):
  #map_ref = MapsSerializer(many=False, read_only=True)
  #map_ref_id = serializers.PrimaryKeyRelatedField(queryset=Maps.objects.all(), many=False)

  class Meta:
    model=Tokens
    fields=['id','current_map','current_position_x','current_position_y']

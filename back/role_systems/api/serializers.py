from rest_framework import serializers
from django.conf import settings
from role_systems.models import *
    

class RoleSystemsSerializer(serializers.ModelSerializer):

  class Meta:
    model=RoleSystems
    fields="__all__"
      
from rest_framework import serializers
from django.conf import settings
from rune_quest.models import *


class CategoryModifiersSerializer(serializers.ModelSerializer):

  class Meta:
    model = Categories
    fields = '__all__'


class CharacterSkillsSerializer(serializers.ModelSerializer):
  category = CategoryModifiersSerializer(many=False, read_only=True)
  category_id = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all(), many=False)

  class Meta:
    model = CharacterSkills
    fields="__all__"


class RacesSerializer(serializers.ModelSerializer):

  class Meta:
    model=Races
    fields=['id', 'race', 'move_rates', 'creation_points']


class RuneQuestSerializer(serializers.ModelSerializer):
  race = RacesSerializer(many=False, read_only=True)
  #race_id = serializers.PrimaryKeyRelatedField(queryset=Races.objects.all(), many=False)

  class Meta:
    model=RuneQuest
    fields="__all__"
      

class SkillsSerializer(serializers.ModelSerializer):
  category = CategoryModifiersSerializer(many=False, read_only=True)
  category_id = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all(), many=False)

  class Meta:
    model = Skills
    fields="__all__"


class SkillsModifiersSerialzer(serializers.ModelSerializer):
  character = RuneQuestSerializer(many=False, read_only=True)
  character_id = serializers.PrimaryKeyRelatedField(queryset=RuneQuest.objects.all(), many=False)

  class Meta:
    model=SkillsModifiers
    fields='__all__'

    
class CheckedWeaponsAttackSkillsSerializer(serializers.ModelSerializer):

  class Meta:
    models=WeaponsSkills
    fields='__all__'


class CheckedParrySkillsSerializer(serializers.ModelSerializer):

  class Meta:
    models=WeaponsSkills
    fields='__all__'


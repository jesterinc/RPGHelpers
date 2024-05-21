from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework import status

#from django.http import Http404
#from django.shortcuts import get_object_or_404
#from rest_framework import viewsets
#from django.conf import settings
#from rest_framework.permissions import  BasePermission
#from django.db.models import Q
      
from rune_quest.models import *
from rune_quest.api.serializers import *
      
import json
import random


class CategoriesDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):
    """
    CategoriesDetailView(APIView) get

    Contains: pk

    """
    try:

      categories = Categories.objects.get(pk=pk)
      context = {'request': request}
      results = CategoriesSerializer(categories, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = CategoriesSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      categories = Categories.objects.get(pk=pk)
      serializer = CategoriesSerializer(categories, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      categories = Categories.objects.get(pk=pk)
      categories.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class CategoriesList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    categories_list = Categories.objects.filter()
    categories_serializer = CategoriesSerializer(categories_list, many=True, context=context).data

    return Response(categories_serializer)


class CategoryModifiersDetailsView(APIView):
  permission_classes = []
  
  def get(self, request, pk):

    try:

      category_modifier = Categories.objects.get(pk=pk)
      context = {'request': request}
      results = CategoryModifiersSerializer(category_modifier, many=False, context=context).data
      
      return Response(results, status=status.HTTP_201_CREATED)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self,request):

    data = request.data
    serializer = CategoryModifiersSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryModifiersList(APIView):
  permission_classes = []

  def get(self,request):

    context = {'request': request}
    category_modifiers = Categories.objects.all().order_by("category")
    category_modifiers_serializer = CharacterSkillsSerializer(category_modifiers, many=True, context=context).data

    return Response(category_modifiers_serializer)


class CharacterSkillsDetailsView(APIView):
  permission_classes = []

  def get(self,request,pk):

    try:

      character_skills = CharacterSkills.objects.get(pk=pk)
      context = {'request': request}
      results = CharacterSkillsSerializer(character_skills, many=False, context=context).data
      
      return Response(results, status=status.HTTP_201_CREATED)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self,request):

    data = request.data
    serializer = CharacterSkillsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      character_skills = CharacterSkills.objects.get(pk=pk)
      serializer = CharacterSkillsSerializer(character_skills, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      character_skills = CharacterSkills.objects.get(pk=pk)
      character_skills.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class CharacterSkillsList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    character_skills = CharacterSkills.objects.filter(deleted=False).order_by("race")
    character_skills_serializer = CharacterSkillsSerializer(character_skills, many=True, context=context).data

    return Response(character_skills_serializer)


class GetCheckedSkillsDetailView(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    skills = CharacterSkills.objects.filter(checked=True)
    skills_checked = SkillsSerializer(skills, many=True, context=context).data

    return Response(skills_checked)


class GetCheckedWeaponSkillsDetailView(APIView):

  def get(self, request):

    weapons_skills_checked = []
    context = {'request': request}
    weapons_attack_skills = WeaponsSkills.objects.filter(checked_attack=True)
    checked_parry_skills = WeaponsSkills.objects.filter(checked_parry=True)
    weapons_skills_checked.append({'weapons_attack': CheckedWeaponsAttackSkillsSerializer(weapons_attack_skills, many=True, context=context).data})
    weapons_skills_checked.append({'checked_parry': CheckedParrySkillsSerializer(checked_parry_skills, many=True, context=context).data})

    return Response(weapons_skills_checked)


class MagicsDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):
    """
    MagicsDetailView(APIView) get

    Contains: pk

    """
    try:

      magics = Magics.objects.get(pk=pk)
      context = {'request': request}
      results = MagicsSerializer(magics, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = MagicsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      magics = Magics.objects.get(pk=pk)
      serializer = MagicsSerializer(magics, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      magics = Magics.objects.get(pk=pk)
      magics.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class MagicsList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    magics_list = Magics.objects.filter()
    magics_serializer = MagicsSerializer(magics_list, many=True, context=context).data

    return Response(magics_serializer)


class MagicSpellsDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):
    """
    MagicSpellsDetailView(APIView) get

    Contains: pk

    """
    try:

      magic_spells = MagicSpells.objects.get(pk=pk)
      context = {'request': request}
      results = MagicSpellsSerializer(magic_spells, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = MagicSpellsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      magic_spells = MagicSpells.objects.get(pk=pk)
      serializer = MagicSpellsSerializer(magic_spells, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      magic_spells = MagicSpells.objects.get(pk=pk)
      magic_spells.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class MagicSpellsList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    magic_spells_list = MagicSpells.objects.filter()
    magic_spells_serializer = MagicSpellsSerializer(magic_spells_list, many=True, context=context).data

    return Response(magic_spells_serializer)


class RacesDetailsView(APIView):
  permission_classes = []

  def get(self,request,pk):

    try:

      race = Races.objects.get(pk=pk)
      context = {'request': request}
      results = RacesSerializer(race, many=False, context=context).data
      
      return Response(results, status=status.HTTP_201_CREATED)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self,request):

    data = request.data
    serializer = RacesSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      race = Races.objects.get(pk=pk)
      serializer = RacesSerializer(race, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      race = Races.objects.get(pk=pk)
      race.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class RacesList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    races = Races.objects.filter(deleted=False).order_by("race")
    races_serializer = RacesSerializer(races, many=True, context=context).data

    return Response(races_serializer)


class RollCharacteristics(APIView):
  permission_classes = []

  def get(self,request,race):

    try:

      race_data = Races.objects.get(pk=race)
      
      characteristics = {
        'str': self.calculate(race_data.dies[0]),
        'con': self.calculate(race_data.dies[1]),
        'siz': self.calculate(race_data.dies[2]),
        'int': self.calculate(race_data.dies[3]),
        'pow': self.calculate(race_data.dies[4]),
        'dex': self.calculate(race_data.dies[5]),
        'app': self.calculate(race_data.dies[6]),
      }

      return Response(characteristics)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)     

  def calculate(self,attribute):

    result = 0
    
    for die in range(attribute['dies_number']):
    
      result += random.randrange(1, attribute['faces'])

    return result + attribute['plus'] - attribute['minus']


class RollDice(APIView):
  permission_classes = []

  def get(self,request,faces, value):

    if faces == 100:

      result = {
        'critical_success': False,
        'special_success': False,
        'success': False,
        'failure': False,
        'fumble': False,
      }

      decimal_die = str(random.randrange(0,10))
      units_die = str(random.randrange(1,10))
      result_die = decimal_die + units_die

      if decimal_die == '0' and units_die == '0':

        result_die = "100"

      skill_result = SkillResults.objects.get(actual_skill=value)

      if int(result_die) <= skill_result.critical_success:

        result['critical_success'] = True

      if int(result_die) <= skill_result.special_success:

        result['special_success'] = True

      if int(result_die) <= value:

        result['success'] = True

      if int(result_die) > value:

        result['failure'] = True

      if int(result_die) > skill_result.fumble:

        result['fumble'] = True

      return Response({"result": result_die, "success_failure": result})

    return Response(None)


class RuneQuestDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):
    """
    RuneQuestDetailView(APIView) get

    Contains: pk

    """
    try:

      runequest = RuneQuest.objects.get(pk=pk)
      context = {'request': request}
      results = RuneQuestSerializer(runeques, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = RuneQuestSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      runequest = RuneQuest.objects.get(pk=pk)
      serializer = RuneQuestSerializer(runeques, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      runequest = RuneQuest.objects.get(pk=pk)
      runeques.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class RuneQuestList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    runequest = RuneQuest.objects.filter()
    rune_quest_serializer = RuneQuestSerializer(runequest, many=True, context=context).data

    return Response(rune_quest_serializer)


class SkillsDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):
    """
    SkillsDetailView(APIView) get

    Contains: pk

    """
    try:

      skills = Skills.objects.get(pk=pk)
      context = {'request': request}
      results = SkillsSerializer(skills, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = SkillsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, skill_id, character_id):

    try:
    
      data = request.data
      skills = Skills.objects.get(skill_id=skill_id, character_id=character_id)
      serializer = SkillsSerializer(skills, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      skills = Skills.objects.get(pk=pk)
      skills.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class SkillsList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    skills_list = Skills.objects.filter()
    skills_serializer = SkillsSerializer(skills_list, many=True, context=context).data

    return Response(skills_serializer)


class SkillsModifiersDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):
    """
    SkillsDetailView(APIView) get

    Contains: pk

    """
    try:

      skills_modifiers = SkillsModifiers.objects.get(pk=pk)
      context = {'request': request}
      results = SkillsModifiersSerializer(skills_modifiers, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 


  def post(self, request):
    """
    SkillsModifiers(APIView) post

    request.data contains
      'pk',    Integer
      'str',   Integer
      'con',   Integer
      'siz',   Integer
      'int',   Integer
      'pow',   Integer
      'dex',   Integer
      'app',   Integer
    """

    data = request.data
    
    strength = data['str']
    constitution = data['con']
    size = data['siz']
    intelligence = data['int']
    power = data['pow']
    dexterity = data['dex']
    appearance = data['app']

    modifiers = {
      'agility': self.calc_modifier('primary', dexterity) + self.calc_modifier('secondary', strength) + self.calc_modifier('negative', size),
      'communication': self.calc_modifier('primary', intelligence) + self.calc_modifier('secondary', power) + self.calc_modifier('secondary', appearance),
      'knowledge': self.calc_modifier('primary', intelligence),
      'magical': self.calc_modifier('primary',intelligence) + self.calc_modifier('primary', power) + self.calc_modifier('secondary', dexterity),
      'manipulation': self.calc_modifier('primary', intelligence) + self.calc_modifier('primary', dexterity) + self.calc_modifier('secondary', strength),
      'perception': self.calc_modifier('primary', intelligence) + self.calc_modifier('secondary', power) + self.calc_modifier('secondary', constitution),
      'stealth': self.calc_modifier('primary', dexterity) + self.calc_modifier('negative', size) + self.calc_modifier('negative', power),
    }

    SkillsModifiers.objects.update_or_create(character_id=data['pk'] ,defaults=modifiers)

    return Response(modifiers)

  def calc_modifier(self, kind, value):

    result = 0

    if kind == 'primary':

      if int(value) < 10:

        result = (10 - int(value)) * -1

      elif int(value) > 10:

        result = (int(value) - 10)

    elif kind == 'secondary':

      if int(value) > 10:

        result = (int(value) - 10) // 2

      elif int(value) < 10:

        result = ((10 - int(value)) // 2) * -1

    elif kind == 'negative':
      
      if int(value) > 10:

        result = (int(value) - 10) * -1

      elif int(value) < 10:

        result = (10 - int(value))

    return result


class SkillsModifierslList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    skills_modifier_list = SkillsModifiers.objects.filter()
    skills_modifiers_serializer = SkillsSerializer(skills_modifier_list, many=True, context=context).data

    return Response(skills_serializer)


class WeaponsDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):
    """
    WeaponsDetailView(APIView) get

    Contains: pk

    """
    try:

      weapons = Weapons.objects.get(pk=pk)
      context = {'request': request}
      results = WeaponsSerializer(weapons, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = WeaponsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      weapons = Weapons.objects.get(pk=pk)
      serializer = WeaponsSerializer(weapons, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      weapons = Weapons.objects.get(pk=pk)
      weapons.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class WeaponsList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    weapons_list = Weapons.objects.filter()
    weapons_serializer = WeaponsSerializer(weapons_list, many=True, context=context).data

    return Response(weapons_serializer)


class WeaponCategoriesDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):
    """
    WeaponCategoriesDetailView(APIView) get

    Contains: pk

    """
    try:

      weapon_categories = WeaponCategories.objects.get(pk=pk)
      context = {'request': request}
      results = WeaponCategoriesSerializer(weapon_categories, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = WeaponCategoriesSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      weapon_categories = WeaponCategories.objects.get(pk=pk)
      serializer = WeaponCategoriesSerializer(weapon_categories, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      weapon_categories = WeaponCategories.objects.get(pk=pk)
      weapon_categories.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class WeaponCategoriesList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    weapon_categories_list = WeaponCategories.objects.filter()
    weapon_categories_serializer = WeaponCategoriesSerializer(weapon_categories_list, many=True, context=context).data

    return Response(weapon_categories_serializer)


class WeaponModifiersDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):
    """
    WeaponModifiersDetailView(APIView) get

    Contains: pk

    """
    try:

      weapon_modifiers = WeaponModifiers.objects.get(pk=pk)
      context = {'request': request}
      results = WeaponModifiersSerializer(weapon_modifiers, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = WeaponModifiersSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      weapon_modifiers = WeaponModifiers.objects.get(pk=pk)
      serializer = WeaponModifiersSerializer(weapon_modifiers, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      weapon_modifiers = WeaponModifiers.objects.get(pk=pk)
      weapon_modifiers.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class WeaponModifiersList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    weapon_modifiers_list = WeaponModifiers.objects.filter()
    weapon_modifiers_serializer = WeaponModifiersSerializer(weapon_modifiers_list, many=True, context=context).data

    return Response(weapon_modifiers_serializer)


class WeaponSkillsDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):
    """
    WeaponModifiersDetailView(APIView) get

    Contains: pk

    """
    try:

      weapon_skills = WeaponSkills.objects.get(pk=pk)
      context = {'request': request}
      results = WeaponSkillsSerializer(weapon_skills, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = WeaponSkillsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      weapon_skills = WeaponModifiers.objects.get(pk=pk)
      serializer = WeaponSkillsSerializer(weapon_skills, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      weapon_skills = WeaponSkills.objects.get(pk=pk)
      weapon_skills.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class WeaponSkillsList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    weapon_skills_list = WeaponSkills.objects.filter()
    weapon_skills_serializer = WeaponSkillsSerializer(weapon_skills_list, many=True, context=context).data

    return Response(weapon_skills_serializer)





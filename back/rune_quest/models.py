from django.db import models
from django.conf import settings

from players.models import Players
from campaigns.models import Campaigns

# Create your models here.

class Categories(models.Model):

  category = models.CharField(max_length=50)
  base_value = models.IntegerField(default=0)

  class Meta:
    managed = True
    db_table = "rq_categories"


class CharacterSkills(models.Model):

  character = models.ForeignKey("RuneQuest", related_name="CharactersSkills_RuneQuest", on_delete=models.CASCADE)
  skill = models.ForeignKey("SkillsModifiers", related_name="CharactersSkills_SkillsModifiers", on_delete=models.CASCADE)
  value = models.IntegerField(default=0)
  annotations = models.CharField(max_length=300, null=True, blank=True)
  checked = models.BooleanField(default=False)

  class Meta:
    managed = True
    db_table = "rq_character_skills"


class Magic(models.Model):

  character = models.ForeignKey("RuneQuest", related_name="Magic_RuneQuest",on_delete=models.CASCADE)
  base_value = models.IntegerField(default=0)
  ceremony = models.IntegerField(default=0)
  enchant = models.IntegerField(default=0)
  summon = models.IntegerField(default=0)
  duration = models.IntegerField(default=0)
  intensity = models.IntegerField(default=0)
  multispell = models.IntegerField(default=0)
  spell_range = models.IntegerField(default=0)

  class Meta:
    managed = True
    db_table = "rq_magic"


class MagicSpells(models.Model):

  character = models.ForeignKey("RuneQuest", related_name="MagicSpells_RuneQuest",on_delete=models.CASCADE)
  spell_name = models.CharField(max_length=200)
  value = models.IntegerField(default=0)
  checked = models.BooleanField(default=False)

  class Meta:
    managed = True
    db_table = "rq_magic_spells"


class Races(models.Model):

  race = models.CharField(max_length=30)
  dies = models.JSONField([{"attribute": "str", "faces": 6, "dies_number": 3, "plus": 0, "minus": 0},{"attribute": "con", "faces": 6, "dies_number": 3, "plus": 0, "minus": 0},{"attribute": "siz", "faces": 6, "dies_number": 2, "plus": 6, "minus": 0},{"attribute": "int", "faces": 6, "dies_number": 2, "plus": 6, "minus": 0},{"attribute": "pow", "faces": 6, "dies_number": 3, "plus": 0, "minus": 0},{"attribute": "dex", "faces": 6, "dies_number": 3, "plus": 0, "minus": 0},{"attribute": "app", "faces": 6, "dies_number": 3, "plus": 0, "minus": 0}])
  move_rates = models.IntegerField(default=2)
  creation_points = models.IntegerField(default=300)
  active = models.BooleanField(default=True)
  deleted = models.BooleanField(default=False)

  class Meta:
    managed = True
    db_table = "rq_races"


class RuneQuest(models.Model):

  adventurer_name = models.CharField(max_length=50, null=True,blank=True)
  player_name = models.ForeignKey(Players, related_name="RuneQuest_Players", on_delete=models.PROTECT, null=True,blank=True)
  campaign = models.ForeignKey(Campaigns, related_name="RuneQuest_Campaigns", on_delete=models.PROTECT, null=True,blank=True)
  homeland_clan = models.CharField(max_length=50, null=True,blank=True)
  age = models.IntegerField(default=0, null=True,blank=True)
  gender = models.CharField(max_length=3, choices=(('ply','player'),('mtr','master'),('bth','both')), null=True,blank=True)
  parent_occupation = models.CharField(max_length=50, null=True,blank=True)
  culture = models.CharField(max_length=50, null=True,blank=True)
  adventurer_occupation = models.CharField(max_length=50, null=True,blank=True)
  religion = models.CharField(max_length=50, null=True,blank=True)
  free = models.CharField(max_length=100, null=True,blank=True)
  current_str = models.IntegerField(default=8)
  original_str = models.IntegerField(default=8)
  current_con = models.IntegerField(default=8)
  original_con = models.IntegerField(default=8)
  current_siz = models.IntegerField(default=8)
  original_siz = models.IntegerField(default=8)
  current_int = models.IntegerField(default=8)
  original_int = models.IntegerField(default=8)
  current_pow = models.IntegerField(default=8)
  original_pow = models.IntegerField(default=8)
  current_dex = models.IntegerField(default=8)
  original_dex = models.IntegerField(default=8)
  current_app = models.IntegerField(default=8)
  original_app = models.IntegerField(default=8)
  damage_modifier = models.IntegerField(default=8)
  move_rate = models.IntegerField(default=8)
  dex_srm = models.IntegerField(default=8)
  siz_srm = models.IntegerField(default=8)
  magic_points = models.IntegerField(default=0)
  fatigue_points = models.IntegerField(default=0)
  hit_points = models.IntegerField(default=0)
  skills = models.JSONField({}, null=True,blank=True)
  magic = models.JSONField({}, null=True,blank=True)
  weapons_skills = models.JSONField({}, null=True,blank=True)
  hit_points_locations = models.JSONField({}, null=True,blank=True)
  notes = models.TextField(null=True,blank=True)
  active = models.BooleanField(default=True)
  deleted = models.BooleanField(default=False)

  class Meta:
    managed = True
    db_table = "rune_quest"


class Skills(models.Model):

  category = models.ForeignKey("Categories", related_name="Skills_Categories", on_delete=models.PROTECT, null=True, blank=True)
  skill = models.CharField(max_length=300)
  base_value = models.IntegerField(default=0)
  status = models.BooleanField(default=False)

  class Meta:
    managed = True
    db_table = "rq_skills"


class SkillResults(models.Model):

  actual_skill = models.IntegerField(default=0)
  critical_success = models.IntegerField(default=0, null=True)
  special_success = models.IntegerField(default=0, null=True)
  fumble = models.IntegerField(default=0, null=True)

  class Meta:
    managed = True
    db_table = "rq_skill_result"


class SkillsModifiers(models.Model):

  character = models.ForeignKey("RuneQuest", related_name="CategoryModifiers_RuneQuest", on_delete=models.CASCADE)
  agility = models.IntegerField(default=0)
  communication = models.IntegerField(default=0)
  knowledge = models.IntegerField(default=0)
  magical = models.IntegerField(default=0)
  manipulation = models.IntegerField(default=0)
  perception = models.IntegerField(default=0)
  stealth = models.IntegerField(default=0)

  class Meta:
    managed = True
    db_table = "rq_skills_modifiers"


class Weapons(models.Model):

  category = models.ForeignKey("WeaponCategories", related_name="Weapons_WeaponCategories", on_delete=models.PROTECT)
  weapon = models.CharField(max_length=100)
  damage  = models.CharField(max_length=20)
  min_str = models.IntegerField(default=0)
  min_dex = models.IntegerField(default=0)
  enc  = models.IntegerField(default=0)
  base_chance = models.IntegerField(default=0)
  armor_points = models.IntegerField(default=0)
  strike_rank = models.IntegerField(default=0)
  weapon_range_effective = models.IntegerField(default=0)
  weapon_range_max = models.IntegerField(default=0)
  weapon_rate_of_fire = models.CharField(max_length=10)
  price = models.IntegerField(default=0)

  class Meta:
    managed = True
    db_table = "rq_weapons"


class WeaponCategories(models.Model):

  weapon_category = models.CharField(max_length=150)

  class Meta:
    managed = True
    db_table = "rq_weapon_categories"


class WeaponModifiers(models.Model):

  character = models.ForeignKey("RuneQuest", related_name="WeaponModifiers_RuneQuest",on_delete=models.CASCADE)
  attack_mod = models.IntegerField(default=0)
  parry_mod = models.IntegerField(default=0)

  class Meta:
    managed = True
    db_table = "rq_weapon_modifiers"


class WeaponsSkills(models.Model):

  character = models.ForeignKey("RuneQuest", related_name="WeaponSkills_RuneQuest",on_delete=models.CASCADE)
  weapon = models.ForeignKey("Weapons", related_name="WeaponsCarried_Weapons",on_delete=models.CASCADE)
  strike_rank = models.IntegerField(default=0)
  damage = models.IntegerField(default=0)
  attack = models.IntegerField(default=0)
  parry = models.IntegerField(default=0)
  armor_points = models.IntegerField(default=0)
  checked_attack = models.BooleanField(default=False)
  checked_parry = models.BooleanField(default=False)

  class Meta:
    managed = True
    db_table = "rq_weapon_skills"

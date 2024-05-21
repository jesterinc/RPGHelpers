from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rune_quest.api import views

router=DefaultRouter()

### TODO: Must be completed and checked URLS and created SERIALIZERS for new models


urlpatterns = [
  path("rune_quest/CategoryModifiersDetails/", views.CategoryModifiersDetailsView.as_view(), name="runequest-category-modifiers"),
  path("rune_quest/CategoryModifiersDetails/<int:pk>", views.CategoryModifiersDetailsView.as_view(), name="runequest-category-modifiers"),
  path("rune_quest/CategoryModifiersList/", views.CategoryModifiersList.as_view(), name="runequest-category-modifiers-list"),
  path("rune_quest/CharacterSkillsDetails/", views.CharacterSkillsDetailsView.as_view(), name="runequest-character-skills"),
  path("rune_quest/CharacterSkillsDetails/<int:pk>/", views.CharacterSkillsDetailsView.as_view(), name="runequest-character-skills"),
  path("rune_quest/CharacterSkillsList/", views.CharacterSkillsList.as_view(), name="runequest-character-skills-list"),
  path("rune_quest/getCheckedSkills/", views.GetCheckedSkillsDetailView.as_view(), name="runequest-get-checked-skills"),  
  path("rune_quest/getCheckedWeaponSkills/", views.GetCheckedWeaponSkillsDetailView.as_view(), name="runequest-get-checked-weapons-skills"),  
  path("rune_quest/MagicDetail/", views.MagicsDetailView.as_view(), name="magic-details"),
  path("rune_quest/MagicDetail/<int:pk>/", views.MagicsDetailView.as_view(), name="magic-details"),
  path("rune_quest/MagicList/", views.MagicsList.as_view(), name="magic-list"),
  path("rune_quest/RacesDetailsView/", views.RacesDetailsView.as_view(), name="runequest-races-details"),
  path("rune_quest/RacesDetailsView/<int:pk>/", views.RacesDetailsView.as_view(), name="runequest-races-details"),
  path("rune_quest/RacesList/", views.RacesList.as_view(), name="runequest-races-list"),
  path("rune_quest/RollCharacteristics/<str:race>/", views.RollCharacteristics.as_view(), name="runequest-roll-characteristics"),
  path("rune_quest/RollDice/<int:faces>/<int:value>/", views.RollDice.as_view(), name="runequest-roll-dice"),
  path("rune_quest/RuneQuestDetail/", views.RuneQuestDetailView.as_view(), name="runequest-details"),
  path("rune_quest/RuneQuestDetail/<int:pk>/", views.RuneQuestDetailView.as_view(), name="runequest-details"),
  path("rune_quest/RuneQuestList/", views.RuneQuestList.as_view(), name="runequest-list"),
  path("rune_quest/SkillsDetail/", views.SkillsDetailView.as_view(), name="skills-detail"),
  path("rune_quest/SkillsDetail/<int:pk>/", views.SkillsDetailView.as_view(), name="skills-detail"),
  path("rune_quest/SkillsDetail/<int:skill_id>/<int:character_id>/", views.SkillsDetailView.as_view(), name="skills-detail"),
  path("rune_quest/SkillsList/", views.SkillsList.as_view(), name="skills-list"),
  path("rune_quest/SkillsModifiersDetail/", views.SkillsModifiersDetailView.as_view(), name="runequest-skills-modifiers"),  
  path("rune_quest/SkillsModifiersDetail/<int:pk>/", views.SkillsModifiersDetailView.as_view(), name="runequest-skills-modifiers"),  
  path("rune_quest/SkillsModifiersList/", views.SkillsModifierslList.as_view(), name="runequest-skills-modifiers"),  
  path("rune_quest/SkillsResultsDetail/", views.SkillsDetailView.as_view(), name="skill-results-detail"),
  path("rune_quest/SkillsResultsDetail/<int:pk>/", views.SkillsDetailView.as_view(), name="skill-results-detail"),
  path("rune_quest/SkillsResultsDetail/<int:pk>/", views.SkillsDetailView.as_view(), name="skill-results-detail"),
  path("rune_quest/SkillsResultsList/", views.SkillsList.as_view(), name="skill-results-list"),
  path("rune_quest/WeaponsDetail/", views.WeaponsDetailView.as_view(), name="weapons-details"),
  path("rune_quest/WeaponsDetail/<int:pk>/", views.WeaponsDetailView.as_view(), name="weapons-details"),
  path("rune_quest/WeaponsList/", views.WeaponsList.as_view(), name="weapons-list"),
  path("rune_quest/WeaponCategoriesDetail/", views.WeaponCategoriesDetailView.as_view(), name="weapon-categories-details"),
  path("rune_quest/WeaponCategoriesDetail/<int:pk>/", views.WeaponCategoriesDetailView.as_view(), name="weapon-categories-details"),
  path("rune_quest/WeaponCategoriesList/", views.WeaponCategoriesList.as_view(), name="weapon-categories-list"),
  path("rune_quest/WeaponModifiersDetail/", views.WeaponModifiersDetailView.as_view(), name="weapons-modifilers-details"),
  path("rune_quest/WeaponModifiersDetail/<int:pk>/", views.WeaponModifiersDetailView.as_view(), name="weapons-modifiers-details"),
  path("rune_quest/WeaponsModifiersList/", views.WeaponModifiersList.as_view(), name="weapons-modifiers-list"),
  path("rune_quest/WeaponSkillsDetail/", views.WeaponSkillsDetailView.as_view(), name="weapons-skills-details"),
  path("rune_quest/WeaponSkillsDetail/<int:pk>/", views.WeaponSkillsDetailView.as_view(), name="weapons-skills-details"),
  path("rune_quest/WeaponSkillsList/", views.WeaponSkillsList.as_view(), name="weapons-skills-list"),
]








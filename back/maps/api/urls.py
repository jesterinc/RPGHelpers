from django.urls import include, path
from rest_framework.routers import DefaultRouter
from maps.api import views

router=DefaultRouter()


urlpatterns = [
  path("maps/MapsDetails/<int:pk>/", views.MapsDetails.as_view(), name="maps-details"),
  path("maps/MapsDetails/", views.MapsDetails.as_view(), name="maps-details"),
  path("maps/MapsList/", views.MapsList.as_view(), name="maps-list"),
  path("maps/SetActualMap/<int:pk>/", views.SetActualMap.as_view(), name="set-actual-map"),
  path("maps/ObstaclesDetails/", views.ObstaclesDetails.as_view(), name="obstacles-details"),
  path("maps/ObstaclesDetails/<int:pk>/", views.ObstaclesDetails.as_view(), name="obstacles-details"),
  path("maps/ObstaclesList/", views.ObstaclesList.as_view(), name="obstacles_list"),
  path("maps/ProtectionsDetails/", views.ProtectionsDetails.as_view(), name="protections-details"),
  path("maps/ProtectionsDetails/<int:pk>/", views.ProtectionsDetails.as_view(), name="protections-details"),
  path("maps/ProtectionsList/", views.ProtectionsList.as_view(), name="protections-list"),
  path("maps/ProtectionFactorsDetails/", views.ProtectionFactorsDetails.as_view(), name="protection-factors-details"),
  path("maps/ProtectionFactorsDetails/<int:pk>/", views.ProtectionFactorsDetails.as_view(), name="protection-factors-details"),
  path("maps/ProtectionFactorsList/", views.ProtectionFactorsList.as_view(), name="protection-factors-list"),
]


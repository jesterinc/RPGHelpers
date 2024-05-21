from django.urls import include, path
from rest_framework.routers import DefaultRouter
from savage_worlds.api import views

router=DefaultRouter()

urlpatterns = [
  path("savage_worlds/SavageWorldsDetail/<int:pk>/", views.SavageWorldsDetailView.as_view(), name="savageworlds-details"),
  path("savage_worlds/SavageWorldsDetail/", views.SavageWorldsDetailView.as_view(), name="savageworlds-details"),
  path("savage_worlds/SavageWorldsList/", views.SavageWorldsList.as_view(), name="savageworlds-list"),
]
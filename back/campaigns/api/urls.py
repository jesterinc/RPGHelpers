from django.urls import include, path
from rest_framework.routers import DefaultRouter
from campaigns.api import views

router=DefaultRouter()

urlpatterns = [
  path("campaigns/CampaignsDetail/<int:pk>/", views.CampaignsDetailView.as_view(), name="campaigns-details"),
  path("campaigns/CampaignsDetail/", views.CampaignsDetailView.as_view(), name="campaigns-details"),
  path("campaigns/CampaignsList/", views.CampaignsList.as_view(), name="campaigns-list"),
]
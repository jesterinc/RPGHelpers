from django.urls import include, path
from rest_framework.routers import DefaultRouter
from players.api import views

router=DefaultRouter()

urlpatterns = [
  path("players/PlayersDetail/<int:pk>/", views.PlayersDetailView.as_view(), name="players-details"),
  path("players/PlayersDetail/", views.PlayersDetailView.as_view(), name="players-details"),
  path("players/PlayersList/", views.PlayersList.as_view(), name="players-list"),
]
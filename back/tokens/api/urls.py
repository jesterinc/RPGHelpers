from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tokens.api import views

router=DefaultRouter()

urlpatterns = [
  path("tokens/TokensDetails/<int:pk>/", views.TokensDetails.as_view(), name="tokens-details"),
  path("tokens/TokensDetails/", views.TokensDetails.as_view(), name="tokens-details"),
  path("tokens/TokensList/", views.TokensList.as_view(), name="tokens-list"),
  path("tokens/TokensPositionsDetails/<int:pk>/", views.TokensPositionsDetails.as_view(), name="tokens-details"),
  path("tokens/TokensPositionsDetails/", views.TokensPositionsDetails.as_view(), name="tokens-details"),
  path("tokens/TokensPositionsList/", views.TokensPositionsList.as_view(), name="tokens-list"),
]
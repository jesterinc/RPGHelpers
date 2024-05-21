from django.urls import include, path
from rest_framework.routers import DefaultRouter
from role_systems.api import views

router=DefaultRouter()

urlpatterns = [
  path("role_systems/RoleSystemsDetail/<int:pk>/", views.RoleSystemsDetailView.as_view(), name="rolesystems-details"),
  path("role_systems/RoleSystemsDetail/", views.RoleSystemsDetailView.as_view(), name="rolesystems-details"),
  path("role_systems/RoleSystemsList/", views.RoleSystemsList.as_view(), name="rolesystems-list"),
]
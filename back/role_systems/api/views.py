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
      
from role_systems.models import RoleSystems
from role_systems.api.serializers import  RoleSystemsSerializer
      
class RoleSystemsDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:

      rolesystem = RoleSystems.objects.get(pk=pk)
      context = {'request': request}
      results = RoleSystemsSerializer(rolesystem, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = RoleSystemsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      rolesystem = RoleSystems.objects.get(pk=pk)
      serializer = RoleSystemsSerializer(rolesystem, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      rolesystem = RoleSystems.objects.get(pk=pk)
      rolesystem.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class RoleSystemsList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    rolesystems = RoleSystems.objects.filter()
    role_systems_serializer = RoleSystemsSerializer(rolesystems, many=True, context=context).data

    return Response(role_systems_serializer)


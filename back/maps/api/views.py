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
      
from maps.models import Maps, Obstacles, Protections, ProtectionsFactors
from maps.api.serializers import *

class MapsDetails(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:
      
      maps = Maps.objects.get(pk=pk)
      context = {'request': request}
      results = MapsSerializer(maps, many=False, context=context).data

      return Response(results, status=status.HTTP_200_OK)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def post(self, request):

    data = request.data.dict()
    serializer = MapWriteSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      map = Maps.objects.get(pk=pk)
      map.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class MapsList(APIView):
  permissions_classes = []

  def get(self, request):

    context = {'request': request}
    maps = Maps.objects.filter()
    maps_serializer = MapsSerializer(maps, many=True, context=context).data

    return Response(maps_serializer)


class ObstaclesDetails(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:
      
      obstacle = Obstacles.objects.get(pk=pk)
      context = {'request': request}
      results = ObstaclesSerializer(obstacle, many=False, context=context).data

      return Response(results, status=status.HTTP_200_OK)

    except Exception as e:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def post(self, request):

    data = request.data
    serializer = ObstaclesSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      obstacle_name = Obstacles.objects.get(pk=pk)
      serializer = ObstaclesSerializer(obstacle_name, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      obstacle = Obstacles.objects.get(pk=pk)
      obstacle.deleted = True
      obstacle.save()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class ObstaclesList(APIView):
  permissions_classes = []

  def get(self, request):

    context = {'request': request}
    obstacles = Obstacles.objects.filter()
    obstacles_serializer = ObstaclesSerializer(obstacles, many=True, context=context).data

    return Response(obstacles_serializer)


class ProtectionsDetails(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:
      
      protection = Protections.objects.get(pk=pk)
      context = {'request': request}
      results = ProtectionsSerializer(protection, many=False, context=context).data

      return Response(results, status=status.HTTP_200_OK)

    except Exception as e:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def post(self, request):

    data = request.data
    serializer = ProtectionsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      protection_name = Protections.objects.get(pk=pk)
      serializer = ProtectionsSerializer(protection_name, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      protection = Protections.objects.get(pk=pk)
      protection.deleted = True
      protection.save()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class ProtectionsList(APIView):
  permissions_classes = []

  def get(self, request):

    context = {'request': request}
    protections = Protections.objects.filter()
    protections_serializer = ProtectionsSerializer(protections, many=True, context=context).data

    return Response(protections_serializer)


class ProtectionFactorsDetails(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:
      
      protection = ProtectionFactors.objects.get(pk=pk)
      context = {'request': request}
      results = ProtectionFactorsSerializer(protection, many=False, context=context).data

      return Response(results, status=status.HTTP_200_OK)

    except Exception as e:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def post(self, request):

    data = request.data
    serializer = ProtectionFactorsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      protection_name = ProtectionFactors.objects.get(pk=pk)
      serializer = ProtectionFactorsSerializer(protection_name, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      protection = ProtectionFactors.objects.get(pk=pk)
      protection.deleted = True
      protection.save()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class ProtectionFactorsList(APIView):
  permissions_classes = []

  def get(self, request):

    context = {'request': request}
    protections = ProtectionFactors.objects.filter()
    protections_serializer = ProtectionFactorsSerializer(protections, many=True, context=context).data

    return Response(protections_serializer)


class SetActualMap(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:

      selected_map = Maps.objects.get(pk=pk)

      print(f"campaign {selected_map.campaign}")

      for m in Maps.objects.filter(campaign=selected_map.campaign):

        m.actual = False
        m.save()
        
      selected_map.actual = True
      selected_map.save()

      return Response("OK", status=status.HTTP_200_OK)
      
    except Exception as ex:

      return Response(str(ex), status=status.HTTP_404_NOT_FOUND)


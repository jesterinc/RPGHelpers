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
      
from savage_worlds.models import SavageWorlds
from savage_worlds.api.serializers import  SavageWorldsSerializer
      
class SavageWorldsDetailView(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:

      savageworld = SavageWorlds.objects.get(pk=pk)
      context = {'request': request}
      results = SavageWorldsSerializer(savageworld, many=False, context=context).data
      
      return Response(results)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST) 

  def post(self, request):

    data = request.data
    serializer = SavageWorldsSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):

    try:
    
      data = request.data
      savageworld = SavageWorlds.objects.get(pk=pk)
      serializer = SavageWorldsSerializer(savageworld, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      savageworld = SavageWorlds.objects.get(pk=pk)
      savageworld.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class SavageWorldsList(APIView):
  permission_classes = []

  def get(self, request):

    context = {'request': request}
    savageworlds = SavageWorlds.objects.filter()
    savage_worlds_serializer = SavageWorldsSerializer(savageworlds, many=True, context=context).data

    return Response(savage_worlds_serializer)


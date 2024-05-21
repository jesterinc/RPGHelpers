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
      
from tokens.models import *
from tokens.models import Maps
from tokens.api.serializers import *


class TokensDetails(APIView):
  permission_classes = []

  def get(self, request, pk):

    try:
      
      token = Tokens.objects.get(pk=pk)
      context = {'request': request}
      results = TokensSerializer(token, many=False, context=context).data

      return Response(results, status=status.HTTP_200_OK)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def post(self, request):

    data = request.data.dict()
    serializer = TokenWriteSerializer(data=data)
    
    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):

    try:

      token = Tokens.objects.get(pk=pk)
      token.delete()

      return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class TokensList(APIView):
  permissions_classes = []

  def get(self, request):

    context = {'request': request}
    tokens = Tokens.objects.filter()
    tokens_serializer = TokensSerializer(tokens, many=True, context=context).data

    return Response(tokens_serializer)

class TokensPositionsDetails(APIView):
  permission_classes = []

  """
  def get(self, request, pk):

    try:
      
      token = Tokens.objects.get(pk=pk)
      context = {'request': request}
      results = TokensPositionSerializer(token, many=False, context=context).data

      return Response(results, status=status.HTTP_200_OK)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

  def post(self, request):

    data = request.data
    serializer = TokenPositionsSerializers(data=data)

    if serializer.is_valid():

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
  """
  def patch(self, request, pk):

    try:
    
      data = request.data
      token = Tokens.objects.get(pk=pk)
      serializer = TokenPositionSerializer(token, data=data, partial=True)

      if serializer.is_valid():

        serializer.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:

      return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)    


class TokensPositionsList(APIView):
  permissions_classes = []

  def get(self, request):

    context = {'request': request}
    tokens = Tokens.objects.filter()
    tokens_serializer = TokensSerializer(tokens, many=True, context=context).data

    return Response(tokens_serializer)

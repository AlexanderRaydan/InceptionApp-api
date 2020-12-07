
from django.shortcuts import render , redirect
from django.views import generic

from core.serializer import InceptionImageSerializer
from core.inception import interception

from .models import InceptionImageModel

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view


class InceptionImagesViewSet(viewsets.ModelViewSet):

    queryset = InceptionImageModel.objects.all()
    serializer_class = InceptionImageSerializer


@api_view(['GET'])
def Inception(request , id):

    image = InceptionImageModel.objects.get(pk = id)
    name , percentage = interception(image)

    return Response({
        'name' : name,
        'porcentage': percentage
    })
      
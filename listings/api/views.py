from django.shortcuts import render
from rest_framework import viewsets
from .models import House
from .serializers import HouseSerializer

class HouseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

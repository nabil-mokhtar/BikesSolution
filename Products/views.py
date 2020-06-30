from django.shortcuts import render
from rest_framework import viewsets
from .models import branches, Bike, Service, accessories
from .serializers import Branchesserializers, Bikeserializers, Serviceserializers, accessoriesserializers

# Create your views here.


class Branchesview(viewsets.ModelViewSet):
    queryset = branches.objects.all()
    serializer_class = Branchesserializers


class Bikeview(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = Bikeserializers


class Serviceview(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = Serviceserializers


class Accessoriesview(viewsets.ModelViewSet):
    queryset = accessories.objects.all()
    serializer_class = accessoriesserializers

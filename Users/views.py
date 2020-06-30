from django.shortcuts import render
from rest_framework import viewsets
from .models import User, RentReservations, FixReservations
from .serializers import Userserializers, RentReservationsserializers, FixReservationsserializers

# Create your views here.


class userview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializers


class RentReservationsview(viewsets.ModelViewSet):
    queryset = RentReservations.objects.all()
    serializer_class = RentReservationsserializers


class FixReservationsview(viewsets.ModelViewSet):
    queryset = FixReservations.objects.all()
    serializer_class = FixReservationsserializers

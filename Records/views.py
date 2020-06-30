from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.


class RentRecordsview(viewsets.ModelViewSet):
    queryset = models.RentRecords.objects.all()
    serializer_class = serializers.RentRecordsserializers


class FixRecordsview(viewsets.ModelViewSet):
    queryset = models.FixRecords.objects.all()
    serializer_class = serializers.FixRecordsserializers


class SellBRecordview(viewsets.ModelViewSet):
    queryset = models.SellBRecord.objects.all()
    serializer_class = serializers.SellBRecordserializers


class SellARecordview(viewsets.ModelViewSet):
    queryset = models.SellARecord.objects.all()
    serializer_class = serializers.SellARecordserializers


class Noterecordview(viewsets.ModelViewSet):
    queryset = models.Noterecord.objects.all()
    serializer_class = serializers.Noterecordserializers

from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class RentRecordsview(viewsets.ModelViewSet):
    queryset = models.RentRecords.objects.all()
    serializer_class = serializers.RentRecordsserializers
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # def list(self, request):
    #     newest = self.get_queryset() # .order_by('created').last()
    #     # serializer = self.get_serializer_class()(newest)
    #     # return Response(serializer.data)
    #     return Response('newest')

    # def create(self, request):
    #     # new=models.RentRecords()
    #     # new.customer=models.RentUser(id=1)
    #     # new.bike= models.Bike(id=1)
    #     # new.starts= request.POST['starts']
    #     # new.ends= request.POST['ends']
    #     # new.status= request.POST['status'] #must be post-now
    #     # new.note= request.POST['note']
    #     # new.price= request.POST['price']
    #     # new.save()
    #     return Response('hello')

    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    # def destroy(self, request, pk=None):
    #     pass
    def close(request):
         new=models.RentRecords(id= 1)
         bike= models.Bike(id=1)
         return HttpResponse(str(bike.model))
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

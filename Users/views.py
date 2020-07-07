from django.shortcuts import render
from rest_framework import viewsets
from .models import User, RentReservations, FixReservations
from .serializers import Userserializers, RentReservationsserializers, FixReservationsserializers

# Create your views here.


class userview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializers
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

class RentReservationsview(viewsets.ModelViewSet):
    queryset = RentReservations.objects.all()
    serializer_class = RentReservationsserializers


class FixReservationsview(viewsets.ModelViewSet):
    queryset = FixReservations.objects.all()
    serializer_class = FixReservationsserializers

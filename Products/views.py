from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Bike, Service, accessories
from .serializers import Bikeserializers, Serviceserializers, accessoriesserializers
from rest_framework.decorators import action
from django.http import HttpResponse
#import qrcode
# Create your views here.


class Bikeview(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Bike.objects.all()
    serializer_class = Bikeserializers

    #
    # def QR(request):
    #     id=request.POST['id']
    #
    #     #qrcode generator
    #     qr=qrcode.QRCode(version=1,box_size=10,border=5)
    #     data=""+id
    #     qr.add_data(data)
    #     qr.make(fit=True)
    #     img=qr.make_image(fill="black",back_color="white")
    #     url="QR/"+data+".png"
    #     img.save(url)
    #    # img.show()
    #     return HttpResponse(img)

    # img.save("image", format=None)
    # has img


class Serviceview(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Service.objects.all()
    serializer_class = Serviceserializers


class Accessoriesview(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = accessories.objects.all()
    serializer_class = accessoriesserializers
    # has img
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


def home(request):
    return render(request, 'Products/index.html')


def Product_list(request):
    Product_list = Bike.objects.all()
    context = {
        'products': Product_list,
    }
    return render(request, 'Products/buy.html', context)


def rent(request):
    Rent_list = Bike.objects.all()
    print(Rent_list)
    context = {
        'Rent': Rent_list,
    }
    return render(request, 'Products/rent.html', context)


def Product_detail(request, id):
    Product_detail = Bike.objects.get(id=id)
    context = {
        'product': Product_detail
    }
    return render(request, 'Products/displayproduct.html', context)

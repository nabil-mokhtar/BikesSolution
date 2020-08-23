from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Bike, Service, accessories, BikeImage
from .serializers import Bikeserializers, Serviceserializers, accessoriesserializers
from rest_framework.decorators import action
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail
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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        find_us = request.POST['find-us']
        news = request.POST['news']
        message = request.POST['message']

        send_mail(name, message,
                  email, [settings.EMAIL_HOST_USER])

    first_products = Bike.objects.all().order_by('id')
    first_products = first_products[:3]

    last_products = Bike.objects.all().order_by('-id')
    last_products = last_products[:6]

    context = {
        'first_products': first_products,
        'last_products': last_products,
    }
    return render(request, 'Products/index.html', context)


def Product_list(request):
    Product_list = Bike.objects.all().order_by('-id')
    service = Service.objects.all().order_by('-id')

    # search_term = ''
    # if 'search' in request.GET:
    #     search_term = request.GET['search']
    #     Product_list = Product_list.filter(model__icontains=search_term)

    # paginator = Paginator(Product_list, 1)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'products': Product_list,
        'service': service,
        # 'search_term': search_term,
    }
    return render(request, 'Products/Buy_1.html', context)


def rent(request):
    Rent_list = Bike.objects.filter(rentability=True).order_by('-id')
    service = Service.objects.all().order_by('-id')

    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        Rent_list = Rent_list.filter(model__icontains=search_term)

    paginator = Paginator(Rent_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Rent': page_obj,
        'service': service,
        'search_term': search_term,
    }
    return render(request, 'Products/Rent_1.html', context)


def Product_detail(request, id):

    first_products = Bike.objects.all().order_by('id')
    first_products = first_products[:3]

    Product_detail = Bike.objects.get(id=id)
    photos = BikeImage.objects.filter(Bike=Product_detail)
    service = Service.objects.all().order_by('-id')
    context = {
        'product': Product_detail,
        'service': service,
        'photos': photos,
        'first_products': first_products,
    }
    return render(request, 'Products/display_product.html', context)


def contact(request):
    return render(request, 'Products/contact.html')


def account(request):
    return render(request, 'Products/sign-in.html')


def addtocart(request):
    return render(request, 'Products/cart.html')


def error_404_view(request, exception):
    return render(request, 'Products/page404.html')

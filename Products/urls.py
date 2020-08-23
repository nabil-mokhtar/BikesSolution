from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Products'

router = routers.DefaultRouter()
router.register('Bike', views.Bikeview)
router.register('Service', views.Serviceview)
router.register('Accessories', views.Accessoriesview)

urlpatterns = [
    path('api', include(router.urls)),
    #  path('bike/QR',views.Bikeview.QR)
    path('', views.home, name='home'),
    path('product', views.Product_list, name='product_list'),
    path('Rent', views.rent, name='rent_list'),
    path('product/<int:id>', views.Product_detail, name='Product_detail'),
    path('contactus', views.contact, name='contact'),
    path('account', views.account, name='account'),
    path('Cart', views.addtocart, name='cart'),
]

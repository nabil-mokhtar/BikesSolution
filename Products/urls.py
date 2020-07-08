from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Branches', views.Branchesview)
router.register('Bike', views.Bikeview)
router.register('Service', views.Serviceview)
router.register('Accessories', views.Accessoriesview)

urlpatterns = [
    path('', include(router.urls)),
  #  path('bike/QR',views.Bikeview.QR)
]

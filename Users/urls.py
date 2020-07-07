from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('User', views.userview)
router.register('RentReservations', views.RentReservationsview)
router.register('FixReservations', views.FixReservationsview)

urlpatterns = [
    path('', include(router.urls))
]

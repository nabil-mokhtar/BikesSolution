from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('RentRecords', views.RentRecordsview)
router.register('FixRecords', views.FixRecordsview)
router.register('SellBRecord', views.SellBRecordview)
router.register('SellARecord', views.SellARecordview)
router.register('Noterecord', views.Noterecordview)

urlpatterns = [
    path('', include(router.urls))
]

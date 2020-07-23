from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('FixRecords', views.FixRecordsview)
router.register('SellRecord', views.SellRecordview)
router.register('Noterecord', views.Noterecordview)

urlpatterns = [
    path('', include(router.urls)),
    path('RentRecords/<str:qr>/', views.RentRecordDetails.as_view()),
    path('RentRecords/', views.RentRecordsview.as_view()),
    # path('RentRecords/', views.RentRecordsview.as_view())
]

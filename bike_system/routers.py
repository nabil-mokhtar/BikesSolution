from shop.api.viewsets import RentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('rent1', RentViewSet)
